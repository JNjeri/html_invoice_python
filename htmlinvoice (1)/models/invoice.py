from peewee import (Model, CharField, SqliteDatabase,
                    IntegrityError, IntegerField, TextField)

DATABASE = SqliteDatabase("invoice.db")


class Invoice(Model):
    user_email = CharField(max_length=100)
    design_fee = IntegerField()
    hosting_fee = IntegerField()
    domain_fee = IntegerField()
    developer_fee = IntegerField()

    class Meta:
        database = DATABASE