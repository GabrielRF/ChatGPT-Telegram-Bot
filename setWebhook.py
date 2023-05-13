import os
import sys
import telebot

TOKEN = os.getenv('TOKEN')
WEBHOOK = sys.argv[1]

bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()
bot.set_webhook(WEBHOOK)
