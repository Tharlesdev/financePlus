from src.app.externals.db.connection import SessionLocal
from src.app.externals.models.user import User

class UserRepository:
    def create_user(self, data):
        session = SessionLocal()
        user = User(
            name=data["name"],
            email_address=data["email_address"],
            password=data["password"]
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        session.close()
        return user.as_dict

    def get_all_users(self):
        session = SessionLocal()
        users = session.query(User).all()
        session.close()
        return [u.as_dict for u in users]

    def get_user_by_id(self, user_id):
        session = SessionLocal()
        user = session.get(User, user_id)
        session.close()
        return user.as_dict if user else None

    def update_user(self, user_id, data):
        session = SessionLocal()
        user = session.get(User, user_id)
        if not user:
            session.close()
            return None

        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        session.commit()
        session.refresh(user)
        session.close()
        return user.as_dict

    def delete_user(self, user_id):
        session = SessionLocal()
        user = session.get(User, user_id)
        if not user:
            session.close()
            return False
        session.delete(user)
        session.commit()
        session.close()
        return True
