from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import client_type_controller
from t08_flask_mysql.app.my_project.auth.domain import ClientType

client_type_bp = Blueprint('client-types', __name__, url_prefix='/client-types')


@client_type_bp.get('')
def get_all_client_types() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(client_type_controller.find_all()), HTTPStatus.OK)


@client_type_bp.post('')
def create_client_type() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    client_type = ClientType.create_from_dto(content)
    client_type_controller.create(client_type)
    return make_response(jsonify(client_type.put_into_dto()), HTTPStatus.CREATED)


@client_type_bp.get('/<int:client_type_id>')
def get_client_type(client_type_id: int) -> Response:
    """
    Gets client_type by ID.
    :return: Response object
    """
    return make_response(jsonify(client_type_controller.find_by_id(client_type_id)), HTTPStatus.OK)


@client_type_bp.put('/<int:client_type_id>')
def update_client_type(client_type_id: int) -> Response:
    """
    Updates client_type by ID.
    :return: Response object
    """
    content = request.get_json()
    client_type = ClientType.create_from_dto(content)
    client_type_controller.update(client_type_id, client_type)
    return make_response("Client updated", HTTPStatus.OK)


@client_type_bp.patch('/<int:client_type_id>')
def patch_client_type(client_type_id: int) -> Response:
    """
    Patches client_type by ID.
    :return: Response object
    """
    content = request.get_json()
    client_type_controller.patch(client_type_id, content)
    return make_response("Client updated", HTTPStatus.OK)


@client_type_bp.delete('/<int:client_type_id>')
def delete_client_type(client_type_id: int) -> Response:
    """
    Deletes client_type by ID.
    :return: Response object
    """
    client_type_controller.delete(client_type_id)
    return make_response("Client deleted", HTTPStatus.OK)
