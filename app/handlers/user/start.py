from aiogram import Bot, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.db.functions import User
from app.sdk.main import API

router = Router()
api = API()


@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    user_id = message.from_user.id
    msg = await bot.send_message(user_id, "🔄 <i>Загрузка...</i>", parse_mode="HTML")

    if not await User.is_registered(user_id):
        await bot.edit_message_text(
            "🔄 <i>Создание кошелька...</i>", user_id, msg.message_id
        )
        wallet = await api.create_wallet()
        await User.register(user_id, wallet["address"]["pbc"], wallet["address"]["pve"])

        await bot.edit_message_text(
            f"💰 <b>Кошелек создан!</b>\n\n/wallet - открыть кошелёк",
            user_id,
            msg.message_id,
        )
    else:
        await bot.edit_message_text(
            "💰 <b>Кошелек уже создан!</b>\n\n/wallet - открыть кошелёк",
            user_id,
            msg.message_id,
        )
