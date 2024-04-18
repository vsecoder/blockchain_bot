from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from app.sdk.main import API
from app.db.functions import User
from app.keyboards.inline import wallet_keyboard

router = Router()
api = API()


@router.message(Command(commands=["wallet"]))
async def wallet_handler(message: Message, bot: Bot):
    user_id = message.from_user.id
    user = await User.is_registered(message.from_user.id)
    msg = await bot.send_message(user_id, "🔄 <i>Загрузка...</i>", parse_mode="HTML")

    if not user:
        return await bot.edit_message_text(
            "❌ <b>Кошелек не найден!</b>\n\n/start - создать кошелек",
            user_id,
            msg.message_id,
        )

    wallet = await api.get_wallet(user.public_key, user.private_key)

    await bot.edit_message_text(
        f"💰 <b>Кошелек</b>\n\n<b>Coins:</b> {wallet}",
        user_id,
        msg.message_id,
        reply_markup=wallet_keyboard(),
    )
