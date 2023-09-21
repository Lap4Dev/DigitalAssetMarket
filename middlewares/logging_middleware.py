from datetime import datetime

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

# from keyboards.inline.common import channel_link_kb
from loguru import logger


#  pre-process update
# process update
# pre-process message|callback_query
# filter (lambda)
# handler
# post process message
# post process update


class LoggingMiddleware(BaseMiddleware):
    @staticmethod
    async def logging_message(user_id, user_name, message, log_name='msg'):
        text = f"{datetime.now()} - {user_id} - {user_name} - {log_name}({message})"
        logger.info(text)

    async def on_process_message(self, message: types.Message, data: dict):
        chat_id, username, text = message.chat.id, message.from_user.username, message.text
        await self.logging_message(chat_id, username, text, log_name='msg')

    async def on_process_callback_query(self, callback: types.CallbackQuery, data: dict):
        chat_id, username, query = callback.from_user.id, callback.from_user.username, callback.data
        await self.logging_message(chat_id, username, query, log_name='call_query')



