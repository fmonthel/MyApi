import logging
import json
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_restplus import Resource
from rest_api.api.billing.serializers import user
from rest_api.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('users', description='Operations related to users')

@ns.route('/login')
class LoginCollection(Resource) :
    
    @api.response(400, 'Missing JSON request or parameter(s)')
    @api.response(401, 'Bad Username or Password')
    @api.expect(user)
    def post(self) :
        if not request.is_json:
            return {'error': "Missing JSON in request"}

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username:
            return {'error': "Please provide username"}, 400
        if not password:
            return {'error': "Please provide password"}, 400

        if username != 'test' or password != 'test':
            return {'error': "Bad username and/or password"}, 401

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=username)
        return {'access_token': access_token}, 200