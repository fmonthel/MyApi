import logging
import json

from flask import request
from flask_restplus import Resource
from rest_api.api.billing.business import create_customer, update_customer, delete_customer
from rest_api.api.billing.serializers import customer
from rest_api.api.restplus import api
from rest_api.database.models import Customer

log = logging.getLogger(__name__)

ns = api.namespace('billing/customer', description='Operations related to customers')

@ns.route('/')
class CustomerCollection(Resource):

    @api.marshal_list_with(customer)
    def get(self):
        """
        Returns list of customers
        """
        customers = Customer.query.all()
        return customers
    
    @api.response(201, 'Customer successfully created.')
    @api.expect(customer)
    def post(self) :
        """
        Creates a new customer.
        """
        data = request.json
        create_customer(data)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'Customer not found.')
class CustomerItem(Resource):

    @api.marshal_with(customer)
    def get(self, id):
        """
        Returns a customer.
        """
        return Customer.query.filter(Customer.id == id).one()

    @api.expect(customer)
    @api.response(204, 'Customer successfully updated.')
    def put(self, id):
        """
        Updates a customer.
        """
        data = request.json
        update_customer(id, data)
        return None, 204

    @api.response(204, 'Customer successfully deleted.')
    def delete(self, id):
        """
        Deletes a customer.
        """
        delete_customer(id)
        return None, 204