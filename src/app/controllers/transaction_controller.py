from flask import Blueprint, request, jsonify
from src.app.services.transaction_service import transaction_service, Transaction
from uuid import UUID

transaction_bp = Blueprint("transaction", __name__, url_prefix="/transactions")

@transaction_bp.route("/", methods=["GET"])
def list_transactions():
    filters = request.args.to_dict()
    result = transaction_service.list(filters)
    return jsonify(result), 200
