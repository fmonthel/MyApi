import logging
import json

from flask import request
from flask_restplus import Resource
from rest_api.api.billing.business import create_contract, update_contract, delete_contract
from rest_api.api.billing.serializers import contract
from rest_api.api.restplus import api
from rest_api.database.models import Contract

log = logging.getLogger(__name__)

ns = api.namespace('billing/contract', description='Operations related to contracts')

@ns.route('/')
class ContractCollection(Resource) :

    @api.marshal_list_with(contract)
    def get(self) :
        """
        Returns list of contracts
        """
        contracts = Contract.query.all()
        return contracts

    @api.response(201, 'Contract successfully created.')
    @api.expect(contract)
    def post(self) :
        """
        Creates a new contract.
        """
        data = request.json
        create_contract(data)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'Contract not found.')
class ContractItem(Resource):

    @api.marshal_with(contract)
    def get(self, id):
        """
        Returns a contract.
        """
        return Contract.query.filter(Contract.id == id).one()

    @api.expect(contract)
    @api.response(204, 'Contract successfully updated.')
    def put(self, id):
        """
        Updates a contract.
        """
        data = request.json
        update_contract(id, data)
        return None, 204

    @api.response(204, 'Contract successfully deleted.')
    def delete(self, id):
        """
        Deletes a contract.
        """
        delete_contract(id)
        return None, 204