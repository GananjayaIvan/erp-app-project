from logging.config import fileConfig
import os

from sqlalchemy import create_engine
from alembic import context

from app.db.base import Base
from app.modules.hris.registry import HRIS_MODELS

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_online():
    url = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:secret@db:5432/app_db"
    )

    connectable = create_engine(
        url,
        pool_pre_ping=True
    )

    with connectable.connect() as connection:
        for model in HRIS_MODELS:
            pass

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
            compare_nullable=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    raise Exception("Offline mode not used in Docker")
else:
    run_migrations_online()