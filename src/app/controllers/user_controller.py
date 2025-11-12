from flask import Blueprint, request, jsonify
from src.app.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__)

from flask import Blueprint, request, jsonify
from src.app.services.user_service import UserService

user_bp = Blueprint("user", __name__, url_prefix="/users")
service = UserService()


@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    try:
        user = service.create_user(data)
        return jsonify(user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@user_bp.route("/", methods=["GET"])
def list_users():
    users = service.get_all_users()
    return jsonify(users), 200


@user_bp.route("/<uuid:user_id>", methods=["GET"])
def get_user(user_id):
    user = service.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(user), 200


@user_bp.route("/<uuid:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    try:
        user = service.update_user(user_id, data)
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404
        return jsonify(user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@user_bp.route("/<uuid:user_id>", methods=["DELETE"])
def delete_user(user_id):
    deleted = service.delete_user(user_id)
    if not deleted:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({"message": "Usuário removido com sucesso"}), 200