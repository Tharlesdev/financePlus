from flask import Blueprint, request, jsonify
from src.app.services.transaction_service import service

transaction_bp = Blueprint("transaction", __name__, url_prefix="/transactions")


@transaction_bp.route("/", methods=["GET"])
def list_transactions():
    transactions = service.get_all_transactions()
    return jsonify(transactions), 200


@transaction_bp.route("/<uuid:transaction_id>", methods=["GET"])
def get_transaction(transaction_id):
    transaction = service.get_transaction_by_id(transaction_id)
    if not transaction:
        return jsonify({"error": "Transação não encontrada"}), 404
    return jsonify(transaction), 200


@transaction_bp.route("/", methods=["POST"])
def create_transaction():
    data = request.json
    created = service.create_transaction(data)
    return jsonify(created), 201


@transaction_bp.route("/<uuid:transaction_id>", methods=["PUT"])
def update_transaction(transaction_id):
    data = request.json
    updated = service.update_transaction(transaction_id, data)
    if not updated:
        return jsonify({"error": "Transação não encontrada"}), 404
    return jsonify(updated), 200


@transaction_bp.route("/<uuid:transaction_id>", methods=["DELETE"])
def delete_transaction(transaction_id):
    deleted = service.delete_transaction(transaction_id)
    if not deleted:
        return jsonify({"error": "Transação não encontrada"}), 404
    return jsonify({"message": "Transação removida"}), 200
