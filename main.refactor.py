from telegram import Update, constants
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext
import logging

from classes.Question import Question
from classes.Flow import Flow
from Flows.Flow3 import flow

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your bot token
TOKEN = '7304026680:AAHT8Am89N6s-fYE5FYA799VdboO9V29jbk'
#TOKEN = '7156964389:AAGhnz_ISm7iVWeATkWlkpWCneZoJn2l_f4'
application = Application.builder().token(TOKEN).build()

# # Define your questions
# questions = {
#     "q1": Question(
#         id="q1",
#         text="What is this image?",
#         media="logos.jpeg",
#         media_type="image",
#         options={"A": "q2", "B": "q3"},
#         keyboard_type="inline"
#     ),
#     "q2": Question(
#         id="q2",
#         text="Watch this video and answer:",
#         media="Countdown.mp4",
#         media_type="video",
#         options={"Option 1": "q4", "Option 2": "q5"},
#         keyboard_type="reply"
#     ),
#     "q3": Question(
#         id="q3",
#         text="Watch this video:",
#         media="https://www.youtube.com/watch?v=UfcAVejslrU",
#         media_type="youtube",
#         options={"Option A": "q6", "Option B": "q7"},
#         keyboard_type="inline"
#     ),
#     "q4": Question(
#         id="q4",
#         text="Play this game:",
#         media="https://www.youtube.com/watch?v=UfcAVejslrU",
#         media_type="youtube",
#         options={"Play": "q8"},
#         keyboard_type="reply"
#     )
# }



# Initialize Flow

def getChatID(update):
    if update.callback_query:
        return update.callback_query.message.chat_id
    return update.message.chat_id


async def handle_media(question, update, context) :
    if question:
        # Prepare the text and markup
        text = question.get_question_text()
        markup = question.get_markup()

        # Prepare media based on media type
        media_path = question._media
        media_type = question.get_media_type()
        chat_id = getChatID(update)

        if media_type == 'image':
            await context.bot.send_photo(
                chat_id=chat_id,
                photo=open(media_path, 'rb'),
                caption=text,
                reply_markup=markup
            )
        elif media_type == 'video':
            await context.bot.send_video(
                chat_id=chat_id,
                video=open(media_path, 'rb'),
                caption=text,
                reply_markup=markup
            )
        elif media_type == 'youtube':
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"{text}\n{media_path}",
                reply_markup=markup,
            )
        elif media_type== 'game':
            # Handle game integration here
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"{text}\n{media_path}",
                reply_markup=markup
            )
        elif len(question.get_options()) == 0:
            await context.bot.send_message(chat_id=chat_id, text=text)
        else:
            await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=markup)
        if len(question.get_options()) == 0:
            # if text:
            #     await context.bot.send_message(chat_id=chat_id, text=text)
            await handle_message(update, context)

    else:
        await update.message.reply_text("Sorry, I don't understand that answer.")
async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    flow.start_flow("intro1")  # Start with the first question
    question = flow.get_current_question()
    await handle_media(question, update, context)


def getNextFromAnswer(update, question):
    if len(question.get_options()) == 0:
        return question.next_question_id
    query = update.callback_query
    if query:
        return query.data
    text = update.message.text
    return question.get_next_question(text)
async def handle_message(update: Update, context: CallbackContext) -> None:
    """Handle replies to reply keyboards."""
    answer = getNextFromAnswer(update, flow.get_current_question())
    next_question = flow.move_to_next_question(answer)
    await handle_media(next_question, update, context)

async def handle_callback_query(update: Update, context: CallbackContext) -> None:
    """Handle callback queries from inline keyboards."""
    query = update.callback_query
    answer = query.data
    next_question = flow.move_to_next_question(answer)
    await handle_media(next_question, update, context)

def main() -> None:
    # """Start the bot."""
    # TOKEN = '7304026680:AAHT8Am89N6s-fYE5FYA799VdboO9V29jbk'
    #
    # application = Application.builder().token(TOKEN).build()
    #
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(handle_message))
    application.add_handler(CallbackQueryHandler(handle_callback_query))

    # Start the Bot
    application.run_polling()


if __name__ == '__main__':
    import asyncio

    try:
        asyncio.run(main())
    except KeyboardInterrupt:  # Ignore exception when Ctrl-C is pressed
        pass