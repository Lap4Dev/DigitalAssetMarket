from functools import wraps

from aiogram import types
from loguru import logger


def async_error_handler(func):
    @wraps(func)
    async def wrapper(message_or_query, *args, **kwargs):
        try:
            return await func(message_or_query, *args, **kwargs)
        except Exception as e:
            handler_name = f"{func.__module__}.{func.__name__}"
            if isinstance(message_or_query, types.Message):
                user_id = message_or_query.from_user.id
            elif isinstance(message_or_query, types.CallbackQuery):
                user_id = message_or_query.from_user.id
            else:
                user_id = "Unknown"
            logger.error(f"Error in handler: {handler_name} for user {user_id}: {e}")

    return wrapper
