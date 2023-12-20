import asyncio

from aiogram import types


async def disappearing_message(msg: types.Message, text: str, delay_seconds: int = 3):
    try:
        msg_id = await msg.reply(text)
        await asyncio.sleep(delay_seconds)
        await msg_id.delete()
        await msg.delete()
    except:
        ...
