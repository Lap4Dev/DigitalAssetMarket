from functools import wraps
from typing import Optional

from loguru import logger

from ..app_models import TelegramUser


class TelegramUserDAL:

    def __init__(self):
        pass

    @staticmethod
    def dal_logging_decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                handler_name = f"{func.__module__}.{func.__name__}"
                logger.error(f"Error in DAL: {handler_name}| Params: {locals()} | {e}")
                return None

        return wrapper

    @staticmethod
    @dal_logging_decorator
    async def create_user_if_not_exist(user_id: int, username: str) -> Optional[TelegramUser]:
        new_user = TelegramUser.objects.get_or_create(
            user_id=user_id,
            defaults={
                'username': username,
            },
        )

        return new_user

    @staticmethod
    @dal_logging_decorator
    async def select_user_by_id(user_id: int) -> Optional[TelegramUser]:
        return TelegramUser.objects.filter(user_id=user_id).first()
