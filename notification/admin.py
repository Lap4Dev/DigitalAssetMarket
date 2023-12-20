from constants.string import Messages
from data.logger import logger
from data.config import ADMIN_CHANNEL_ID
from loader import bot


async def send_message_to_admin_channel(text: str, **kwargs):
    try:
        await bot.send_message(
            ADMIN_CHANNEL_ID,
            text=text,
            **kwargs
        )
    except Exception as ex:
        logger.error(ex)


async def notify_withdraw_request(
        request_id: int, user_id: int, username: str, withdraw_amount: float, withdraw_address: str,  commission: float
):
    try:
        await send_message_to_admin_channel(
            Messages.withdraw_request_notification(request_id, user_id, username, withdraw_amount, withdraw_address, commission)
        )
    except Exception as ex:
        logger.error(ex)
