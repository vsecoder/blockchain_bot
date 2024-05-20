from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message

from app.sdk.main import API
from app.db.functions import Sponsor

router = Router()
api = API()


@router.message(Command(commands=["sponsors"]))
@router.callback_query(F.data.startswith("get"))
async def sponsor_handler(message: Message, bot: Bot):
    sponsors = await Sponsor.get_all()
    text = "🙏 <b>Список спонсоров</b>\n\n{}\n\n<i>За каждый канал будет ежедневно приходить</i> <code>0.001 minicoin</code>"

    sponsors = "\n".join([f" - @{sponsor.channel_username}" for sponsor in sponsors])

    await bot.send_message(
        message.from_user.id, text.format(sponsors), parse_mode="HTML"
    )
