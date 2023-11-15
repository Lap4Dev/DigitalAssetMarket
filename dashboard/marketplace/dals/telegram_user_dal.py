import dataclasses
from decimal import Decimal
from typing import Optional, Tuple

from . import BaseDAL
from ..app_models import TelegramUser


@dataclasses.dataclass
class ShowUserSchema:
    user_id: Optional[int] = 0
    username: Optional[str] = 'unknown'
    balance: Optional[float] = 0.0
    purchased_files_count: Optional[int] = 0
    sold_files_count: Optional[int] = 0
    user_rating: Optional[float] = 0.0


class TelegramUserDAL:

    def __init__(self):
        pass

    @staticmethod
    @BaseDAL.dal_logging_decorator
    async def create_user_if_not_exist(user_id: int, username: str) -> Tuple[Optional[TelegramUser], bool]:
        new_user, created = TelegramUser.objects.get_or_create(
            user_id=user_id,
            defaults={
                'username': username,
            },
        )

        return new_user, created

    @staticmethod
    @BaseDAL.dal_logging_decorator
    async def get_user_by_id(user_id: int) -> Optional[TelegramUser]:
        return TelegramUser.objects.filter(user_id=user_id).first()

    @staticmethod
    @BaseDAL.dal_logging_decorator
    async def get_user_profile_info_by_id(user_id: int) -> Optional[ShowUserSchema]:
        user = await TelegramUserDAL.get_user_by_id(user_id)
        if user is None:
            return ShowUserSchema()

        return ShowUserSchema(
            user_id=user_id,
            username=user.username,
            balance=float(user.balance),
            purchased_files_count=0,
            sold_files_count=0,
            user_rating=float(user.rating)
        )

    @staticmethod
    @BaseDAL.dal_logging_decorator
    async def get_user_balance_by_id(user_id: int) -> float:
        user = await TelegramUserDAL.get_user_by_id(user_id)
        if user is None:
            return 0

        return float(user.balance)

    @staticmethod
    @BaseDAL.dal_logging_decorator
    async def set_user_balance(user_id: int, amount: Decimal) -> bool:
        """return True if success else False"""
        user: Optional[TelegramUser] = await TelegramUserDAL.get_user_by_id(user_id)
        if user is None:
            return False

        user.balance = amount
        user.save()
        return True
