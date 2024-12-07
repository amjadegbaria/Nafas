from telegram import constants
from utils.helpers import get_chat_id


async def send_media(chat_id, text, markup, media_path, media_type, bot):
    """
    Sends the appropriate media based on the provided media type.
    """
    handlers = {
        'image': lambda: bot.send_photo(chat_id, photo=open(media_path, 'rb'), caption=text, reply_markup=markup),
        'video': lambda: bot.send_video(chat_id, video=open(media_path, 'rb'), caption=text, reply_markup=markup, read_timeout=200),
        'html': lambda: bot.send_message(chat_id, text=f"{text}\n{media_path}", reply_markup=markup, parse_mode=constants.ParseMode.HTML),
        'youtube': lambda: bot.send_message(chat_id, text=f"<a href='{media_path}'> </a>{text}", reply_markup=markup, parse_mode=constants.ParseMode.HTML) if media_path else None,
        'default': lambda: bot.send_message(chat_id, text=f"{text}\n{media_path}", reply_markup=markup, disable_web_page_preview=True),
    }

    handler = handlers.get(media_type, handlers['default'])
    await handler()


async def handle_media_type(question, update, context):
    """
    Prepares and sends the media associated with a question.
    """
    chat_id = get_chat_id(update)
    await send_media(
        chat_id=chat_id,
        text=question.get_question_text(),
        markup=question.get_markup(),
        media_path=question._media,
        media_type=question.get_media_type(),
        bot=context.bot
    )

