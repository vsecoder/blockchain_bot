from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message

from app.commands import owner_commands, users_commands
from app.config import Config
from app.keyboards.inline import get_author_keyboard

router = Router()


@router.message(Command(commands=["help"]))
async def help_handler(message: Message, config: Config):
    text = "ℹ️ <b>Список команд:</b> \n\n"
    commands = (
        owner_commands.items()
        if message.from_user.id == config.settings.owner_id
        else users_commands.items()
    )
    for command, description in commands:
        text += f"/{command} - <b>{description}</b> \n"
    await message.answer(text)


@router.callback_query(F.data.startswith('pay'))
@router.message(Command(commands=["help_pay"]))
async def about_pay_handler(message: Message, bot: Bot):
    bot_information = await bot.get_me()
    await bot.send_message(message.from_user.id,
        "<b>ℹ️ Информация о переводах:</b> \n\n"
        "<i>Перевод осуществляется командой /pay, "
        "которая принимает 2 аргумента:\n"
        "- id пользователя телеграм\n"
        "- сумма, сколько перевести\n\n</i>"
        "<code>/pay 1218845111 10</code>\n"
        "Переведёт пользователю @vsecoder 10 Coins"
    )
