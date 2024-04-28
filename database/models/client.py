from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime


class Client(Model):
    name = CharField()
    email = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
