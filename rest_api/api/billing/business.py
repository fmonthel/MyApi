from rest_api.database import db
from rest_api.database.models import Customer, Contract

def create_contract(data) :
    # Init values
    customer_id = data.get('customer_id')
    customer = Customer.query.filter(Customer.id == customer_id).one()
    monae_quote = data.get('monae_quote')
    monae_invoice = data.get('monae_invoice')
    startdate = data.get('startdate')
    enddate = data.get('enddate')
    flag = data.get('flag')
    sid = data.get('sid')
    # Let's go
    contract = Contract(customer,monae_quote,monae_invoice,startdate,enddate,flag,sid)
    db.session.add(contract)
    db.session.commit()

def update_contract(contract_id, data):
    # Init values
    contract = Contract.query.filter(Contract.id == contract_id).one()
    customer_id = data.get('customer_id')
    contract.customer = Customer.query.filter(Customer.id == customer_id).one()
    contract.monae_quote = data.get('monae_quote')
    contract.monae_invoice = data.get('monae_invoice')
    contract.startdate = data.get('startdate')
    contract.enddate = data.get('enddate')
    contract.flag = data.get('flag')
    contract.sid = data.get('sid')
    # Let's go
    db.session.add(contract)
    db.session.commit()

def delete_contract(contract_id):
    # Let's go
    contract = Contract.query.filter(Contract.id == contract_id).one()
    db.session.delete(contract)
    db.session.commit()

def create_customer(data) :
    # Init values
    monaecustomer_id = data.get('monaecustomer_id')
    unix_id = data.get('unix_id')
    # Let's go
    customer = Customer(monae_customer,unix_id)
    db.session.add(customer)
    db.session.commit()

def update_customer(customer_id, data):
    # Init values
    customer = Customer.query.filter(Customer.id == customer_id).one()
    customer.monaecustomer_id = data.get('monaecustomer_id')
    customer.unix_id = data.get('unix_id')
    # Let's go
    db.session.add(customer)
    db.session.commit()

def delete_customer(customer_id):
    # Let's go
    customer = Customer.query.filter(Customer.id == customer_id).one()
    db.session.delete(customer)
    db.session.commit()