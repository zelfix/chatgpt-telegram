import os

from dotenv import load_dotenv

load_dotenv()

ORG_NAME = os.getenv('ORG_NAME')
API_KEY = os.getenv('API_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

SUPPORTED_MODELS = ["gpt-3.5-turbo", "gpt-4"]
MAX_MESSAGE_COUNT_IN_REQUEST = 5  # How many massages ChatGPT will handle in one request

TG_START_MESSAGE = '''
    Привет! Я телеграм бот, который позволит Вам получить доступ к OpenAI ChatGPT.
    
⚡ Этот бот использует ту же модель, что и [вебсайт](https://chat.openai.com/chat): gpt-3.5-turbo.

Я могу помочь вам в различных областях знаний, включая ответы на вопросы, помощь в поиске информации,
составление планов и стратегий, создание контента и многое другое. Просто опишите, какую помощь вам нужно,
и я постараюсь предоставить наилучшее решение для вашего запроса.

В случае, если нужно сбросить контекст беседы и начать общение с чистого листа, используйте команду [/reset].

Have fun! 😎
'''
