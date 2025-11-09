from flask import Flask

from src.app.externals.db.connection import engine
from src.app.externals.models import Category, Transaction, User
from src.app.externals.models.base import Base


def create_app():
    app = Flask(__name__)

    # Criar todas as tabelas (uma única vez)
    with app.app_context():
        Base.metadata.create_all(bind=engine)

    @app.route("/")
    def home():
        return "FinancePlus API - funcionando! 🚀"

    return app


app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
