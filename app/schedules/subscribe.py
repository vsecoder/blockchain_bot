import logging

from app.db.functions import User, Sponsor
from app.sdk.main import API
from app.config import parse_config

from aiogram import Bot


logger = logging.getLogger(__name__)


async def subscribe_schedule(bot: Bot) -> None:
    """
    Subscribe schedule function
    """
    sponsors = await Sponsor.get_all()
    api = API()
    statistic_claimed = 0
    owner = parse_config().settings.owner_id

    for user in await User.get_all():
        claimed = 0
        for sponsor in sponsors:
            try:
                member = await bot.get_chat_member(sponsor.channel_id, user.telegram_id)
                if member:
                    await api.credit(user.public_key, 0.001)
                    claimed += 0.001
            except Exception as e:
                logger.error(f"Error: {e}")
        await bot.send_message(
            user.telegram_id, f"🔄 <i>Вы получили за подписки {claimed} minicoins</i>"
        )
        statistic_claimed += claimed

    await bot.send_message(
        owner, f"📈 Всего люд за день собрал {statistic_claimed} minicoins"
    )
