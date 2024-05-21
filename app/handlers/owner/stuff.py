import time

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from app.filters.is_owner import IsOwner
from app.db.functions import User
from app.sdk.main import API

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


@router.message(IsOwner(is_owner=True), Command(commands=["recreate_wallets"]))
async def recreate_handler(message: Message, bot: Bot):
    api = API()
    users = await User.get_all()

    for user in users:
        wallet = await api.create_wallet()
        await User.edit_wallet(
            user.telegram_id, wallet["address"]["pbc"], wallet["address"]["pve"]
        )
        await api.credit(wallet["address"]["pbc"], 0.01)

        try:
            await bot.send_message(
                user.telegram_id,
                f"💰 <b>В связи с большой обновой кошельки пересозданы, и всем было начислено 0.01 minicoin",
            )
        except Exception as e:
            pass

    await message.answer("🔄 <b>Кошельки пересозданы!</b>")
