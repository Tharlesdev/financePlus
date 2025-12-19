from flask import Blueprint, jsonify, request
from src.app.services.category_service import service
from src.app.security.auth_required import auth_required

category_bp = Blueprint("category", __name__, url_prefix="/categories")


@category_bp.route("/", methods=["POST"])
@auth_required
def create_category():
    data = request.json

    data["user_id"] = request.user_id

    category = service.create_category(data)

    return jsonify(category), 201


@category_bp.route("/", methods=["GET"])
@auth_required
def list_categories():
    categories = service.get_all_categories()
    return jsonify(categories), 200


@category_bp.route("/<uuid:category_id>", methods=["GET"])
@auth_required
def get_category(category_id):
    category = service.get_category_by_id(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(category), 200


@category_bp.route("/<uuid:category_id>", methods=["PUT"])
@auth_required
def update_category(category_id):
    data = request.get_json()
    category = service.update_category(category_id, data)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(category), 200


@category_bp.route("/<uuid:category_id>", methods=["DELETE"])
@auth_required
def delete_category(category_id):
    success = service.delete_category(category_id)
    if not success:
        return jsonify({"error": "Category not found"}), 404
    return jsonify({"message": "Category deleted"}), 200
