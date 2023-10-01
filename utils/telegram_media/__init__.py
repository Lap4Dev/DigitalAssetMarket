from loguru import logger

from loader import bot


async def send_photo_menu(chat_id, image_path, caption, inline_keyboard):
    try:
        caption = caption
        photo = open(image_path, 'rb')
        await bot.send_animation(chat_id=chat_id, animation=photo, caption=caption, reply_markup=inline_keyboard)
    except Exception as ex:
        logger.error(ex)
