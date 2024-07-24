import logging
import i18n
import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
from Flow import Flow
from Question import Question

# Your bot token
TOKEN = '7445359342:AAFZFe78wVKYh40lo4hTWlMR313uTKEQZl4'
LOCK_FILE = 'bot.lock'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

translator = i18n.Translator('data')

# Initialize Flow and Questions
introFlow = Flow()



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    introFlow.add_question(Question(0, translator.translate('intro'), "", [translator.translate('start')]))
    introFlow.add_question(Question(1, translator.translate('stress_question'), "", [
        translator.translate('stress_option1'),
        translator.translate('stress_option2'),
        translator.translate('stress_option3')
    ]))
    question = introFlow.get_next_question()
    if question:
        if update.message:
            await update.message.reply_text(question.text, reply_markup=question.markup)
        elif update.callback_query:
            await update.callback_query.message.reply_text(question.text, reply_markup=question.markup)
    else:
        if update.message:
            await update.message.reply_text("No more questions.")
        elif update.callback_query:
            await update.callback_query.message.reply_text("No more questions.")


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    chat_id = query.message.chat_id
    await query.answer()


    # Get the next question
    question = introFlow.get_next_question()
    if question:
        await context.bot.send_message(chat_id=chat_id, text=question.text, reply_markup=question.markup)
    else:
        await context.bot.send_message(chat_id=chat_id, text="No more questions.")


async def default(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await start(update, context)


def main() -> None:
    # Check if lock file exists
    if os.path.exists(LOCK_FILE):
        print("Another instance of the bot is already running.")
        sys.exit(1)

    # Create lock file
    with open(LOCK_FILE, 'w') as f:
        f.write(str(os.getpid()))

    try:
        application = Application.builder().token(TOKEN).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, default))
        application.add_handler(CallbackQueryHandler(button))

        # Start the bot
        application.run_polling()
    finally:
        # Remove lock file on exit
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())