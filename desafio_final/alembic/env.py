import sys
import os
import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context

# Permite importar modules do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ----------------------------
# Importa a Base e os models
# ----------------------------
from workinapi.contrib.repository.models import BaseModel
from workinapi.categorias.models import CategoriaModel
from workinapi.atleta.models import AtletaModel
from workinapi.centro_treinamento.models import CentroTreinamentoModel

# Metadados para geração de migrações
target_metadata = BaseModel.metadata

# ----------------------------
# Configuração Alembic
# ----------------------------
config = context.config

if config.config_file_name:
    fileConfig(config.config_file_name)

# ----------------------------
# Funções para migração offline
# ----------------------------
def run_migrations_offline() -> None:
    """Executa migrações sem conexão com o banco (offline)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# ----------------------------
# Funções para migração online
# ----------------------------
def do_run_migrations(connection):
    """Executa migrações com conexão ativa (sincronamente dentro do async)."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_async():
    """Executa migrações no modo assíncrono (online)."""
    config_section = config.get_section(config.config_ini_section)
    if config_section is None:
        raise RuntimeError("Seção de configuração 'sqlalchemy' não encontrada no alembic.ini")

    connectable = async_engine_from_config(
        config_section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

def run_migrations_online() -> None:
    asyncio.run(run_migrations_async())

# ----------------------------
# Executa conforme o modo
# ----------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
