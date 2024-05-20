import logging

from app.db.functions import User, Sponsor
from datetime import datetime, timedelta

from aiogram import Bot


logger = logging.getLogger(__name__)


async def status_schedule(bot: Bot) -> None:
    """
    Status schedule function
    """
    logger.info("Running status schedule")
