from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
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
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True,  # útil para SQLite, mas seguro deixar ativado
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Executa as migrations no modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True  # útil para FKs com use_alter
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
