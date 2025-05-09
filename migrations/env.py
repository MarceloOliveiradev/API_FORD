from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Importa os metadados dos modelos
from app.models import Base

# Config do Alembic
config = context.config

# Habilita log
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define os metadados para autogenerate funcionar
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Executa as migrations no modo offline."""
    url = os.getenv("DATABASE_URL")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Executa as migrations no modo online."""
    url = os.getenv("DATABASE_URL")
    connectable = create_engine(url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
