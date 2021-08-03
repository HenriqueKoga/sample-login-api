from flask import jsonify

from views.exception import error_bp
from flask_api import status


@error_bp.app_errorhandler(Exception)
def handle_exception(err):
    try:
        response = {
            'error': err.name,
            'description': err.description
        }
        return jsonify(response), err.code
    except Exception:
        return jsonify({'msg': 'Server Error'}), status.HTTP_500_INTERNAL_SERVER_ERROR
