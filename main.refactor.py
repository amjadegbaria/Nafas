from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext
from time import sleep
from telegram import Update, constants
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext, ContextTypes
import logging
from config import TOKEN
import asyncio
from handlers.command_handler import start, restart, default
from handlers.message_handler import handle_message

import i18n
from flows.Flow3 import flow

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

application = Application.builder().token(TOKEN).build()

translator = i18n.Translator('data')


def main() -> None:
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("restart", restart))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, default))
    application.add_handler(CallbackQueryHandler(handle_message))

    # Start the Bot
    application.run_polling()


if __name__ == '__main__':
    # Configure logging

    try:
        asyncio.run(main())
    except KeyboardInterrupt:  # Ignore exception when Ctrl-C is pressed
        pass