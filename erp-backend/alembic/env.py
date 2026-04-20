from logging.config import fileConfig
import os

from sqlalchemy import create_engine
from alembic import context

from app.db.base import Base
import app.models  # IMPORTANT

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_online():
    url = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:secret@db:5432/app_db"
    )

    connectable = create_engine(url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    raise Exception("Offline mode not used in Docker")
else:
    run_migrations_online()