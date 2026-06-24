from pathlib import Path

from app.db.database import DB_PATH, Base, engine
from app.db import models  # importa modelos para que SQLAlchemy registre las tablas


if __name__ == "__main__":
    Path(DB_PATH).touch(exist_ok=True)
    Base.metadata.create_all(bind=engine)
    print(f"DB creada/verificada en: {DB_PATH}")
    print("Tablas creadas/verificadas: conversations, messages")