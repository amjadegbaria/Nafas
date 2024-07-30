import logging
import i18n
from telegram import Update, constants, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
from Flow import Flow
from Question import Question
from Flows import Flow2

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
flow = Flow2.flow
async def handleBotMessage(question: Question, update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    parse_mode = constants.ParseMode.MARKDOWN_V2 if translator.contains_url(question.text) else None
    if len(question.image):
        if question.image.lower().endswith('.mp4'):
            await context.bot.send_video(chat_id=chat_id, video=question.image, caption=question.text)
        else:
            await context.bot.send_photo(chat_id=chat_id, photo=question.image, caption=question.text)
    else:
        if question.id == 'end':
            reply_keyboard = [[str(i) for i in range(1, 6)], [str(i) for i in range(6, 11)]]
            markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            await context.bot.send_message(chat_id=chat_id, text=question.text, reply_markup=markup,
                                           parse_mode=parse_mode)
        else:
            await context.bot.send_message(chat_id=chat_id, text=question.text, reply_markup=question.markup,
                                       parse_mode=parse_mode)
async def handleMessage(question: Question, update: Update):
    parse_mode = constants.ParseMode.MARKDOWN_V2 if translator.contains_url(question.text) else None
    if len(question.image):
        if question.image.lower().endswith('.mp4'):
            await update.message.reply_video(video=question.image, caption=question.text, disable_notification=True, supports_streaming=True)
        else:
            await update.message.reply_photo(photo=question.image, caption=question.text)
    else:
        await update.message.reply_text(question.text, reply_markup=question.markup, parse_mode=parse_mode)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = flow.get_next_question()

    if question and update.message:
        await handleMessage(question, update)

    # handle all questions with no button
    while question and len(question.options) == 0 and question.id != 'end':
        question = flow.get_next_question()
        if question:
            await handleMessage(question, update)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    chat_id = query.message.chat_id
    await query.answer()

    if query.data != 'intro3-0' and query.data != 'intro8-0':
        # Get the next question
        question = flow.get_next_question()
        if question:
            await handleBotMessage(question, update, context)
    elif query.data == 'intro3-0':
        await context.bot.send_message(chat_id=chat_id, text='ووين الصورة؟😉')
    elif query.data == 'intro8-0':
        await context.bot.send_message(chat_id=chat_id, text='سجّلت؟🎤')



    # handle all questions with no button
    while question and len(question.options) == 0 and question.id != 'end':
        question = flow.get_next_question()
        if question:
            await handleBotMessage(question, update, context)


async def default(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.photo:
        await start(update, context)
        # Proceed to the next question or step
    else:
        await update.message.reply_text('That doesn\'t seem to be a photo. Please upload a photo.')

async def recording(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.voice:
        await start(update, context)
        # Proceed to the next question or step
    else:
        await update.message.reply_text('That doesn\'t seem to be a recording. Please upload a recording.')

def main() -> None:
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, default))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.PHOTO, photo))
    application.add_handler(MessageHandler(filters.VOICE, recording))


    # Run the bot
    application.run_polling()


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())