from telegram import constants
from utils.helpers import get_chat_id
import aiofiles


async def send_media(chat_id, text, markup, media_path, media_type, bot):
    """
    Sends the appropriate media based on the provided media type.
    """
    if media_type == 'image':
        async with aiofiles.open(media_path, 'rb') as f:
            photo_data = await f.read()
        await bot.send_photo(chat_id, photo=photo_data, caption=text, reply_markup=markup)
    elif media_type == 'video':
        async with aiofiles.open(media_path, 'rb') as f:
            video_data = await f.read()
        await bot.send_video(chat_id, video=video_data, caption=text, reply_markup=markup, read_timeout=200)
    elif media_type == 'html':
        await bot.send_message(chat_id, text=f"{text}\n{media_path}", reply_markup=markup, parse_mode=constants.ParseMode.HTML)
    elif media_type == 'youtube':
        if media_path:
            await bot.send_message(chat_id, text=f"<a href='{media_path}'> </a>{text}", reply_markup=markup, parse_mode=constants.ParseMode.HTML)
    else:
        await bot.send_message(chat_id, text=f"{text}\n{media_path}", reply_markup=markup, disable_web_page_preview=True)


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

