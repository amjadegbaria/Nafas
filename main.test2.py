import logging
import i18n
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
from Flow import Flow
from Question import Question

# Your bot token
TOKEN = '7304026680:AAHT8Am89N6s-fYE5FYA799VdboO9V29jbk'
application = Application.builder().token(TOKEN).build()
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

translator = i18n.Translator('data')

# Initialize Flow and Questions
flow = Flow()



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    flow.add_question(Question(0, translator.translate('intro'), "", [translator.translate('start')]))
    flow.add_question(Question(1, translator.translate('stress_question'), "", [translator.translate('stress_option1'),
                                                                                translator.translate('stress_option2'),
                                                                                translator.translate(
                                                                                    'stress_option3')]))
    flow.add_question(Question(2, "What is your favorite animal?", "", ["Cat", "Dog", "Bird", "Fish"]))
    flow.add_question(Question(3, "What is your favorite food?", "", ["Pizza", "Burger", "Pasta", "Salad"]))

    question = flow.get_next_question()
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
    question = flow.get_next_question()
    if question:
        await context.bot.send_message(chat_id=chat_id, text=question.text, reply_markup=question.markup)
    else:
        await context.bot.send_message(chat_id=chat_id, text="No more questions.")
        # await application.stop()
        # await application.shutdown()


async def default(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)


def main() -> None:
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, default))
    application.add_handler(CallbackQueryHandler(button))

    # Run the bot
    application.run_polling()


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())