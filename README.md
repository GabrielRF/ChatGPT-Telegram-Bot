<img align="right" alt="Logo ChatGPT e Logo Telegram" width="30%" height="auto" src="https://blog.gabrf.com/assets/img/ChatGPTTelegram.png">

# ChatGPT Telegram Bot

Post sobre o repositório: [blog.gabrf.com/posts/ChatGPTTelegram](https://blog.gabrf.com/posts/ChatGPTTelegram/)

## Requisitos

Listados no arquivo *requirements.txt*
```
pytelegrambotapi==4.11.0
openai==0.27.6
urllib3==1.25.8
```

## Serverless

O deploy deste bot é feito usando [Serverless.com](https://serverless.com).

## Bot

Bot funcionando em uma função Lambda da AWS com webhook.

## setWebhook

Arquivo usado para definir a URL do webhook. É o último passo do deploy.
