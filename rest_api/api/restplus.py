import logging
import traceback
from flask_restplus import Api
from rest_api import settings
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

authorizations = {
    'Bearer' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'Authorization',
    	'description' : 'JWT Authorization header using the Bearer scheme. Example: \"Bearer {token}\"'
    }
}

api = Api(version='1.0', title='Flox-arts.net API', authorizations=authorizations,
          description='API endpoints of Flox-arts.net Organization')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404