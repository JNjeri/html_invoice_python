#!/usr/bin/env python

from flask import (Flask, render_template)
from models.user import User
from models.invoice import Invoice
import bootstrap
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)


@app.route('/')
def index():
    bootstrap.initialize()
    user = User.select().where(
        User.email == "john@doe.com"
    ).get()
    invoice = Invoice.select().where(
        Invoice.user_email == user.email
    ).get()
    total = invoice.hosting_fee + invoice.design_fee + invoice.domain_fee + invoice.developer_fee
    return render_template('invoice.html', user=user, invoice=invoice, total=total)


if __name__ == '__main__':
    app.run(**app_start_config)