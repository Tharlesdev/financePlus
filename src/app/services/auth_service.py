from src.app.externals.db.connection import SessionLocal
from src.app.externals.models.user import User
from src.app.externals.exceptions import PasswordIncorrectException
from src.app.security.jwt_utils import create_token


class AuthService:

    def register(self, data: dict):
        db = SessionLocal()
        try:
            name = data.get("name")
            email = data.get("email")
            password = data.get("password")

            if not name or not email or not password:
                return {"error": "Campos obrigatórios faltando"}, 400

            existing = db.query(User).filter(User.email == email).first()
            if existing:
                return {"error": "E-mail já registrado"}, 409

            user = User(
                name=name,
                email=email,
                password=password
            )

            db.add(user)
            db.commit()
            db.refresh(user)

            return user.as_dict, 201

        finally:
            db.close()

    def login(self, email: str, password: str):
        db = SessionLocal()

        try:
            user = db.query(User).filter(User.email == email).first()
            if not user:
                return None

            user.validate_password(password)
            return user
        
        except PasswordIncorrectException:
            return None
        
        finally:
            db.close()



auth_service = AuthService()
