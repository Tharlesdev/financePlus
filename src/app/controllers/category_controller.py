from flask import Blueprint, jsonify, request
from src.app.services.category_service import service

category_bp = Blueprint("category", __name__, url_prefix="/categories")


@category_bp.route("/", methods=["POST"])
def create_category():
    data = request.get_json()
    category = service.create_category(data)
    return jsonify(category), 201


@category_bp.route("/", methods=["GET"])
def list_categories():
    categories = service.get_all_categories()
    return jsonify(categories), 200


@category_bp.route("/<uuid:category_id>", methods=["GET"])
def get_category(category_id):
    category = service.get_category_by_id(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(category), 200


@category_bp.route("/<uuid:category_id>", methods=["PUT"])
def update_category(category_id):
    data = request.get_json()
    category = service.update_category(category_id, data)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(category), 200


@category_bp.route("/<uuid:category_id>", methods=["DELETE"])
def delete_category(category_id):
    success = service.delete_category(category_id)
    if not success:
        return jsonify({"error": "Category not found"}), 404
    return jsonify({"message": "Category deleted"}), 200
