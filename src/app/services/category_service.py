from src.app.externals.db.connection import SessionLocal
from src.app.externals.models.category import Category
import uuid


class serviceCategory:
    def create_category(self, data):


        db = SessionLocal()
        try:
            if "user_id" in data and isinstance(data["user_id"], str):
                data["user_id"] = uuid.UUID(data["user_id"])
            category = Category(**data)
            db.add(category)
            db.commit()
            db.refresh(category)
            return category.as_dict
        finally:
            db.close()


    def get_all_categories(self):
        db = SessionLocal()
        try:
            categories = db.query(Category).all()
            return [c.as_dict for c in categories]
        finally:
            db.close()


    def get_category_by_id(self, category_id):
        db = SessionLocal()
        try:
            category = db.query(Category).get(category_id)
            return category.as_dict if category else None
        finally:
            db.close()


    def update_category(self, category_id, data):
        db = SessionLocal()
        try:
            category = db.query(Category).get(category_id)
            if not category:
                return None

            for key, value in data.items():
                setattr(category, key, value)

            db.commit()
            db.refresh(category)
            return category.as_dict
        finally:
            db.close()


    def delete_category(self, category_id):
        db = SessionLocal()
        try:
            category = db.query(Category).get(category_id)
            if not category:
                return False

            db.delete(category)
            db.commit()
            return True
        finally:
            db.close()

service = serviceCategory()