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
    @classmethod
    async def is_registered(cls, owner_id: int) -> Union[models.Collection, bool]:
        try:
            return await cls.get(owner_id=owner_id)
        except DoesNotExist:
            return False

    @classmethod
    async def register(cls, owner_id, amount, currency, description):
        await Collection(
            owner_id=owner_id, amount=amount, currency=currency, description=description
        ).save()

    @classmethod
    async def get_all(cls):
        return await cls.all()

    @classmethod
    async def pay(cls, owner_id, amount):
        collection = await cls.get(owner_id)
        collection.amount += amount
        await collection.save()
