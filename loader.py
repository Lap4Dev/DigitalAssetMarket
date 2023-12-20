import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from dashboard.marketplace.dals.telegram_user_dal import TelegramUserDAL
from dashboard.marketplace.dals.wallet_dal import WalletDAL
from data import config
from data.config import I18N_DOMAIN, LOCALES_DIR
from middlewares.localization_middleware import LocalizationMiddleware

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
i18n = LocalizationMiddleware(I18N_DOMAIN, LOCALES_DIR)

_ = i18n.gettext
__ = i18n.lazy_gettext

dp = Dispatcher(bot, storage=MemoryStorage())

telegram_user_dal = TelegramUserDAL()
wallet_dal = WalletDAL()
