from app.db.base import Base
from app.db.session import engine

from app.modules.hris.registry import HRIS_MODELS


def init_db():
    Base.metadata.create_all(bind=engine)