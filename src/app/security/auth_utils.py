import jwt
import datetime
import os
SECRET_KEY = os.getenv("SECRET_KEY") # depois coloque no .env

def create_jwt(user_id: str):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        "iat": datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # expirou
    except jwt.InvalidTokenError:
        return None  # inválido
