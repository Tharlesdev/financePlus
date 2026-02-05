from flask import Blueprint, request, jsonify
from src.app.services.auth_service import auth_service
from src.app.security.auth_required import auth_required
from src.app.security.jwt_utils import create_token
from src.app.externals.db.connection import SessionLocal
from src.app.externals.models.user import User
from uuid import UUID

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "name, email e password são obrigatórios"}), 400

    user, status = auth_service.register(data)

    return jsonify(user), status


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "email e password são obrigatórios"}), 400

    user = auth_service.login(email, password)

    if not user:
        return jsonify({"error": "Credenciais inválidas"}), 401

    # gera token JWT
    token = create_token(user_id=str(user.id))

    return jsonify({
        "access_token": token,
        "token_type": "Bearer"
    }), 200

@auth_bp.route("/me", methods=["GET"])
@auth_required
def me():
    db = SessionLocal()
    try:
        user_id = UUID(request.user_id)  # 🔥 conversão correta

        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "user_id": str(user.id),
            "name": user.name,
            "email": user.email
        }), 200
    finally:
        db.close()
