import openai
import os
import telebot
import time

openai.api_key = os.getenv('CHATGPTKEY')
bot = telebot.TeleBot(os.getenv('TOKEN'), threaded=False)
answer_to = str(os.getenv('USERID'))
messages = []

def ask_chatgpt(message):
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        n = 1,
        temperature = 1,
        max_tokens=1024
    )
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    return response.choices[0].message.content

@bot.message_handler(commands=["start"])
def clean_context(message):
    if str(message.from_user.id) in answer_to:
        messages = []
        bot.reply_to(message, f'Olá! Tudo bem?')

@bot.message_handler(func=lambda message: str(message.from_user.id) in answer_to)
def message_received(message):
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        response = ask_chatgpt(message.text)
    except openai.error.RateLimitError:
        for _ in range(0,3):
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(5)
        response = ask_chatgpt(message.text)
    bot.reply_to(message, response)

def hello_http(event, context):
    update = telebot.types.Update.de_json(event['body'])
    try:
        bot.process_new_updates([update])
    except:
        pass
    return {"statusCode": 200, "body": "hello world"}
