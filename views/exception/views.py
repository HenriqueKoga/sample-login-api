from flask import jsonify

from views.exception import error_bp


@error_bp.app_errorhandler(Exception)
def handle_exception(err):
    response = {
        'error': err.name,
        'description': err.description
    }
    return jsonify(response), err.code
