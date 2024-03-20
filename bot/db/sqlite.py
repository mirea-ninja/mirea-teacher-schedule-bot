import os

from peewee import Model, PrimaryKeyField, SqliteDatabase, TextField

db = SqliteDatabase(os.path.join(os.path.dirname(__file__), "data/bot.db"))


class ScheduleBot(Model):
    id = PrimaryKeyField(unique=True)
    username = TextField(null=True)
    first_name = TextField(null=True)
    last_name = TextField(null=True)
    favorite = TextField(null=True)

    class Meta:
        database = db
