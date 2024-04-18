from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from app.sdk.main import API
from app.db.functions import User
from app.keyboards.inline import wallet_keyboard

router = Router()
api = API()


@router.message(Command(commands=["pay"]))
async def pay_handler(message: Message, bot: Bot):
    args = message.text.split(' ')
    user_id = message.from_user.id
    msg = await bot.send_message(user_id, "🔄 <i>Загрузка...</i>", parse_mode="HTML")

    if len(args) != 3:
        return await bot.edit_message_text(
            "❌ <i>Неприемлимое кол-во аргументов!</i>", user_id, msg.message_id
        )
    if not args[1].isdigit():
        return await bot.edit_message_text(
            "❌ <i>ID должен быть числом!</i>", user_id, msg.message_id
        )
    if not await User.is_registered(args[1]):
        return await bot.edit_message_text(
            "❌ <i>Такого пользователя нету в боте!</i>", user_id, msg.message_id
        )

    try:
        if float(args[2]) < 0.001:
            return await bot.edit_message_text(
                "❌ <i>Минимальный перевод 0.001!</i>", user_id, msg.message_id
            )
    except:
        return await bot.edit_message_text(
            "❌ <i>Проверьте аргументы!</i>", user_id, msg.message_id
        )

    if user_id == int(args[1]):
        return await bot.edit_message_text(
            "❌ <i>Самый умный?</i>", user_id, msg.message_id
        )

    user1 = await User.is_registered(message.from_user.id)
    user2 = await User.is_registered(args[1])

    res = await api.transfer(
        from_=user1.private_key,
        to=user2.public_key,
        amount=args[2]
    )

    await bot.edit_message_text(
        str(res), user_id, msg.message_id
    )
    await bot.send_message(user_id, "💵 <i>Вам поступил перевод!</i>", parse_mode="HTML")
