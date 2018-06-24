# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime
from rest_api.database import db

class Contract(db.Model) :
    __tablename__ = 't_contract'
    id = db.Column(db.Integer, primary_key=True)
    monae_quote = db.Column(db.Integer, unique=True)
    monae_invoice = db.Column(db.Integer, unique=True)
    startdate = db.Column(db.Date)
    enddate = db.Column(db.Date)
    flag = db.Column(db.String(10))
    sid = db.Column(db.Integer, db.ForeignKey('t_contract.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('t_customer.id'))
    customer = db.relationship('Customer', backref=db.backref('contracts', lazy='dynamic'))

    def __init__(self, customer, monae_quote, monae_invoice, startdate, enddate, flag, sid) :
        self.customer = customer
        self.monae_quote = monae_quote
        self.monae_invoice = monae_invoice
        self.startdate = startdate
        self.enddate = enddate
        self.flag = flag
        self.sid = sid

    def __repr__(self) :
        return '<Contract:{}>'.format(self.id)

class Customer(db.Model) :
    __tablename__ = 't_customer'
    id = db.Column(db.Integer, primary_key=True)
    monae_customer = db.Column(db.Integer, unique=True)
    unix_id = db.Column(db.String(50), unique=True)

    def __init__(self, monae_customer, unix_id) :
        self.monae_customer = monae_customer
        self.unix_id = unix_id

    def __repr__(self) :
        return '<Customer:{}>'.format(self.id)