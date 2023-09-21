from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from data.config import AVAILABLE_LANGUAGES, DEFAULT_LANG


class LocalizationMiddleware(I18nMiddleware):
    @staticmethod
    async def on_pre_process_message(message: types.Message, data: dict):
        user = message.from_user
        lang_code = user.language_code \
            if user.language_code and user.language_code in AVAILABLE_LANGUAGES else DEFAULT_LANG

        data['locale'] = lang_code
