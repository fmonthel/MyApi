from flask_restplus import fields
from rest_api.api.restplus import api

customer = api.model('Customer', {
    'id': fields.Integer(readOnly=True, attribute='id', description='The unique identifier of the customer'),
    'monae_customer': fields.Integer(required=False, attribute='monae_customer', description='Customer ID from MonAE application'),
    'unix': fields.String(required=True, attribute='unix_id', description='Unix account of the customer'),
})

contract = api.model('Contract', {
    'id': fields.Integer(readOnly=True, attribute='id', description='The unique identifier of a contract'),
    'flag': fields.String(required=True, attribute='flag', description='Flag of the contract'),
	'startdate': fields.Date(attribute='startdate', description='Start date of the contract'),
	'enddate': fields.Date(attribute='enddate', description='End date of the contract'),
	'monae_quote': fields.Integer(required=False, attribute='monae_quote', description='Quote ID from MonAE application'),
	'monae_invoice': fields.Integer(required=False, attribute='monae_invoice', description='Invoice ID from MonAE application'),
	'customer_unix': fields.String(required=False, attribute='customer.unix_id', description='Unix account of the customer'),
	'customer_monae': fields.Integer(required=False, attribute='customer.monae_customer', description='MonAE ID of the customer'),
	'customer_id': fields.Integer(required=True, attribute='customer_id', description='Flag of the contract'),
    'sid': fields.Integer(required=False, attribute='sid', description='The child contract ID'),
})