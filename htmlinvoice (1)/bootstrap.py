from models.user import User
from models.invoice import Invoice
from peewee import SqliteDatabase, IntegrityError

DATABASE = SqliteDatabase("invoice.db")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Invoice], safe=True)
    try:
        User.create(
            first_name="Felician",
            last_name="Mueni",
            email="john@doe.com",
            company="Acme Corp."
        )
    except IntegrityError:
        pass
    try:
        Invoice.create(
                user_email="john@doe.com",
                design_fee=500,
                hosting_fee=175,
                domain_fee=10,
                developer_fee=400
        )
    except IntegrityError:
        pass
    DATABASE.close()