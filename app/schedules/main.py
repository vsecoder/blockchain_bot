import asyncio
import aioschedule
import logging

from aiogram import Bot

from app.schedules.subscribe import subscribe_schedule
from app.schedules.status import status_schedule

logger = logging.getLogger(__name__)


async def scheduler(bot: Bot) -> None:
    """Run background worker"""
    logger.info("Running background worker")
    # aioschedule.every(1).minutes.do(parser_schedule, bot=bot)
    aioschedule.every().day.at("15:00").do(subscribe_schedule, bot=bot)
    # aioschedule.every().day.at("15:00").do(status_schedule, bot=bot)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
