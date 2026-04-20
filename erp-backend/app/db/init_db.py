from app.db.base import Base
from app.db.session import engine

import app.models  # ensure models are loaded


def init_db():
    Base.metadata.create_all(bind=engine)