from src.app.externals.db.connection import SessionLocal
from src.app.externals.models.transaction import Transaction
from uuid import UUID

class TransactionService:

    def create_transaction(self, data):
        db = SessionLocal()
        try:
            data["user_id"] = UUID(data["user_id"])
            data["category_id"] = UUID(data["category_id"])

            transaction = Transaction(**data)
            db.add(transaction)
            db.commit()
            db.refresh(transaction)
            return transaction.as_dict
        finally:
            db.close()

    def get_all_transactions(self):
        db = SessionLocal()
        try:
            transactions = db.query(Transaction).all()
            return [t.as_dict for t in transactions]
        finally:
            db.close()

    def get_transaction_by_id(self, transaction_id):
        db = SessionLocal()
        try:
            transaction = db.query(Transaction).get(transaction_id)
            return transaction.as_dict if transaction else None
        finally:
            db.close()

    def update_transaction(self, transaction_id, data):
        db = SessionLocal()
        try:
            transaction = db.query(Transaction).get(transaction_id)
            if not transaction:
                return None

            for key, value in data.items():
                setattr(transaction, key, value)

            db.commit()
            db.refresh(transaction)
            return transaction.as_dict
        finally:
            db.close()

    def delete_transaction(self, transaction_id):
        db = SessionLocal()
        try:
            transaction = db.query(Transaction).get(transaction_id)
            if not transaction:
                return False

            db.delete(transaction)
            db.commit()
            return True
        finally:
            db.close()


service = TransactionService()
