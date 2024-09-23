from flows.flow_handler import getNextFromAnswer
from telegram import Update
from telegram.ext import CallbackContext
from flows.Flow3 import flow


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