from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField()
    public_key = fields.CharField(max_length=255, null=True)
    private_key = fields.CharField(max_length=255, null=True)


class Sponsor(Model):
    id = fields.BigIntField(pk=True)
    channel_id = fields.BigIntField()
    channel_username = fields.CharField(max_length=255)


class Collection(Model):
    id = fields.BigIntField(pk=True)
    owner_id = fields.BigIntField()
    amount = fields.FloatField()
    currency = fields.CharField(max_length=255)
    description = fields.TextField()
    history = fields.JSONField()  # история транзакций
