from functools import wraps
from flask import request, jsonify
from auth_utils import decode_jwt

def jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Token não fornecido"}), 401

        try:
            token = auth_header.split(" ")[1]  # "Bearer <token>"
        except:
            return jsonify({"error": "Formato inválido"}), 401

        payload = decode_jwt(token)

        if not payload:
            return jsonify({"error": "Token inválido ou expirado"}), 401

        request.user_id = payload["user_id"]

        return func(*args, **kwargs)

    return wrapper
