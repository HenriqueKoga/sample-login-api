from flask import jsonify, request
from flask_api import status
from flask_jwt_extended import jwt_required
from flask_login import login_required
from models.brand import Brand, brand_schema, brands_schema
from werkzeug.exceptions import BadRequest

from views.brand import brand_bp


@brand_bp.route('/brands', methods=['GET', 'POST'])
@login_required
@jwt_required()
def brands():
    if request.method == 'GET':
        brands = Brand.query.all()
        return jsonify(brands_schema.dump(brands))

    if request.method == 'POST':
        body = request.get_json()

        try:
            name = body['name']
        except KeyError:
            raise BadRequest

        brand = Brand.create(name=name)
        return jsonify(brand_schema.dump(brand)), status.HTTP_201_CREATED


@brand_bp.route('/brands/<brand_id>', methods=['GET', 'DELETE', 'PUT'])
@login_required
def brand(brand_id):
    if request.method == 'GET':
        user = Brand.get(brand_id)
        return jsonify(brand_schema.dump(user))

    if request.method == 'DELETE':
        Brand.delete(brand_id)
        return jsonify({'msg': 'Brand deleted successfully'})

    if request.method == 'PUT':
        body = request.get_json()
        Brand.update(brand_id, **body)
        return jsonify({'msg': 'Brand updated successfully'})
