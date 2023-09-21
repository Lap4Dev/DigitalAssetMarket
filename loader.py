from aiogram import Bot, Dispatcher, types

from data import config
from data.config import I18N_DOMAIN, LOCALES_DIR
from middlewares.localization_middleware import LocalizationMiddleware

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
i18n = LocalizationMiddleware(I18N_DOMAIN, LOCALES_DIR)

_ = i18n.gettext
__ = i18n.lazy_gettext

dp = Dispatcher(bot)
