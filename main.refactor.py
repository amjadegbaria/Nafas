from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext
import logging
from config import TOKEN
import asyncio
from handlers.command_handler import start
from handlers.message_handler import handle_message, handle_callback_query

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# """Start the bot."""
application = Application.builder().token(TOKEN).build()

def main() -> None:

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(handle_message))
    application.add_handler(CallbackQueryHandler(handle_callback_query))

    # Start the Bot
    application.run_polling()


if __name__ == '__main__':
    # Configure logging

    try:
        asyncio.run(main())
    except KeyboardInterrupt:  # Ignore exception when Ctrl-C is pressed
        pass