from typing import Union

from tortoise.exceptions import DoesNotExist

from app.db import models


class User(models.User):
    @classmethod
    async def is_registered(cls, telegram_id: int) -> Union[models.User, bool]:
        try:
            return await cls.get(telegram_id=telegram_id)
        except DoesNotExist:
            return False

    @classmethod
    async def register(cls, telegram_id, public_key, private_key):
        await User(
            telegram_id=telegram_id, public_key=public_key, private_key=private_key
        ).save()

    @classmethod
    async def get_count(cls) -> int:
        return await cls.all().count()

    @classmethod
    async def get_all(cls):
        return await cls.all()

    @classmethod
    async def edit_wallet(cls, telegram_id, public_key, private_key):
        user = await cls.get(telegram_id=telegram_id)
        user.public_key = public_key
        user.private_key = private_key
        await user.save()


class Sponsor(models.Sponsor):
    @classmethod
    async def is_registered(cls, channel_id: int) -> Union[models.Sponsor, bool]:
        try:
            return await cls.get(channel_id=channel_id)
        except DoesNotExist:
            return False

    @classmethod
    async def register(cls, channel_id, channel_username):
        await Sponsor(channel_id=channel_id, channel_username=channel_username).save()

    @classmethod
    async def get_all(cls):
        return await cls.all()


class Collection(models.Collection):
    pass
