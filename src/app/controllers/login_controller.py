from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from src.app.security.auth_utils import create_jwt
from src.app.externals.models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/login")
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    # Buscar usuário
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Credenciais inválidas"}), 401

    token = create_jwt(str(user.id))

    return jsonify({"access_token": token}), 200
