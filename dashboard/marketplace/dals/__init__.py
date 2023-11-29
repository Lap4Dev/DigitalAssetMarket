from functools import wraps

from loguru import logger


class BaseDAL:
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
