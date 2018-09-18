from peewee import (Model, CharField, SqliteDatabase, IntegrityError)

DATABASE = SqliteDatabase("invoice.db")


class User(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    company = CharField(max_length=200)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    try:
        User.create(
            first_name="Felician",
            last_name="Mueni",
            email="john@doe.com",
            company="Acme Corp."
        )
    except IntegrityError:
        pass
    DATABASE.close()