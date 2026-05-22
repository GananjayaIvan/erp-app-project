from app.db.base import Base
from app.db.session import engine
from app.db.hris.registry import HRIS_MODELS


def init_db():
    import app.modules.hris.models  # ensure models are loaded
    Base.metadata.create_all(bind=engine)