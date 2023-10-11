from aiogram import Dispatcher
from loguru import logger


from middlewares.logging_middleware import LoggingMiddleware


async def on_startup(dp: Dispatcher):
    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)
    await setup_middlewares(dp)


async def setup_middlewares(dp: Dispatcher):
    from loader import i18n
    dp.middleware.setup(i18n)
    dp.middleware.setup(LoggingMiddleware())


if __name__ == '__main__':

    from utils import django_configure
    django_configure.configure_django()

    from aiogram.utils import executor
    from handlers import dp

    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    except Exception as err:
        logger.error(err)

