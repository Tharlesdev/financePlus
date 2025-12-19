from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///src/app/externals/db/financeplus.db"

# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Session local (cada requisição Flask pode abrir uma)
SessionLocal = sessionmaker(bind=engine)
