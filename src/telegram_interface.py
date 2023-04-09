import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from settings import TG_START_MESSAGE

from chatgpt import ChatServer

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()


class TelegramBot:
    def __init__(self, token: str, chat_server: ChatServer):
        self.token = token
        self.chat_server = chat_server
        self.app = ApplicationBuilder().token(token).build()
        self.chat_session = None

        start_handler = CommandHandler('start', self.start)
        reset_handler = CommandHandler('reset', self.reset)
        message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), self.message)
        unknown_handler = MessageHandler(filters.COMMAND, self.unknown)


        self.app.add_handler(start_handler)
        self.app.add_handler(reset_handler)
        self.app.add_handler(message_handler)
        self.app.add_handler(unknown_handler)

    def run(self):
        self.app.run_polling()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        tg_chat_id = update.effective_chat.id
        self.chat_session = await self.chat_server.create_chat(chat_id=tg_chat_id)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=TG_START_MESSAGE, parse_mode="Markdown")
        logger.info(f"Start command received: chatid: {update.message.chat_id}")

    async def reset(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.chat_session.reset_messages()
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Весь контекст удален, начинаем новый чат с чистого листа")
        logger.info(f"Reset command received: chatid: {update.message.chat_id}")

    async def message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        response = await self.chat_session.new_message(update.message.text)
        logger.info(f"Message received: chatid: {update.message.chat_id}, message: {update.message.text}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode='Markdown')
        logger.info(f"Answer received: chatid: {update.message.chat_id}, message: {response}")

    async def unknown(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Я не знаю такой команды =(")
        logger.info(f"Unknown command received: chatid: {update.message.chat_id}, command: {update.message.text}")
