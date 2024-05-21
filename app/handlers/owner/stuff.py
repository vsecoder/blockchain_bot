import time

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from app.filters.is_owner import IsOwner
from app.db.functions import User

router = Router()


@router.message(IsOwner(is_owner=True), Command(commands=["ping"]))
async def ping_handler(message: Message):
    start = time.perf_counter_ns()
    reply_message = await message.answer("<code>⏱ Checking ping...</code>")
    end = time.perf_counter_ns()
    ping = (end - start) * 0.000001
    await reply_message.edit_text(
        f"<b>⏱ Ping -</b> <code>{round(ping, 3)}</code> <b>ms</b>"
    )


@router.message(IsOwner(is_owner=True), Command(commands=["send"]))
async def send_handler(message: Message, bot: Bot):
    users = await User.get_all()
    text = message.text.split(" ", 1)[1]
    count = 0

    for user in users:
        try:
            await bot.send_message(user.telegram_id, text)
            count += 1
        except:
            pass

    await message.answer(f"🔄 <i>Сообщение получило {count} человек")
