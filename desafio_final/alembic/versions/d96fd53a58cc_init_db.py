"""init_db

Revision ID: d96fd53a58cc
Revises: 
Create Date: 2025-08-28 22:56:48.720908

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd96fd53a58cc'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Criar tabela categorias
    op.create_table(
        'categorias',
        sa.Column('pk_id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('id', sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint('id'),          # Apenas 'id' como PK
        sa.UniqueConstraint('pk_id'),           # pk_id único para FK
        sa.UniqueConstraint('nome')             # Nome único
    )
    op.create_index(op.f('ix_categorias_pk_id'), 'categorias', ['pk_id'], unique=False)

    # Criar tabela atletas
    op.create_table(
        'atletas',
        sa.Column('pk_id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=100), nullable=False),
        sa.Column('categoria_id', sa.Integer(), nullable=False),
        sa.Column('id', sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(['categoria_id'], ['categorias.pk_id']),  # FK agora funciona
        sa.PrimaryKeyConstraint('pk_id', 'id')  # PK composta
    )
    op.create_index(op.f('ix_atletas_pk_id'), 'atletas', ['pk_id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_atletas_pk_id'), table_name='atletas')
    op.drop_table('atletas')
    op.drop_index(op.f('ix_categorias_pk_id'), table_name='categorias')
    op.drop_table('categorias')
