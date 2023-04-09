import logging

from chatgpt import ChatServer
from settings import ORG_NAME, API_KEY, TELEGRAM_TOKEN
from telegram_interface import TelegramBot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()


def main():
    chat_server = ChatServer(org_name=ORG_NAME, api_key=API_KEY)
    tg = TelegramBot(token=TELEGRAM_TOKEN, chat_server=chat_server)
    tg.run()


if __name__ == '__main__':
    main()
