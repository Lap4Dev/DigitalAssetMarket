from dashboard.marketplace.app_models import Withdraw
from dashboard.marketplace.dals import BaseDAL
from data import config
from loader import telegram_user_dal


class WithdrawDAL:

    def __init__(self):
        pass

    @staticmethod
    @BaseDAL.dal_logging_decorator
    async def make_withdraw_request(
            user_id: int,
            withdraw_amount: float,
            withdraw_address: str
    ) -> Withdraw | None:
        user = await telegram_user_dal.get_user_by_id(user_id)

        withdraw_request = Withdraw.objects.create(
            user=user,
            wallet=withdraw_address,
            amount=withdraw_amount,
            commission=withdraw_amount * config.WITHDRAW_FEE_AMOUNT / 100
        )

        return withdraw_request
