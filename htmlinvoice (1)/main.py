#!/usr/bin/env python

from flask import (Flask, render_template,request)
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

@app.route('/invoice/generate',methods=['POST','GET'])
def generate():
  invoice= dict(request.form.items()) 
  total = (int(invoice.get('design_fee', 30)) + 
          int(invoice.get('hosting_fee',30))+
          int(invoice.get('domain_fee',40))
          )
  return render_template('user_generated_invoice.html',invoice=invoice, total=total)

pass 

@app.route('/invoice/new')
def new_invoice():
  return render_template('invoice_form.html')

if __name__ == '__main__':
    app.run(**app_start_config)