
"""Initial Migration

Revision ID: 210c45f044d9
Revises:
Create Date: 2026-10-19 17:08:37.294135
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# Identificação da migração
revision: str = "210c45f044d9"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Cria as tabelas do banco de dados."""

    # Tabela de usuários
    op.create_table(
        "usuarios",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("nome", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("senha", sa.String(), nullable=True),
        sa.Column("ativo", sa.Boolean(), nullable=True),
        sa.Column("admin", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id")
    )

    # Tabela de pedidos
    op.create_table(
        "pedidos",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("usuario", sa.Integer(), nullable=True),
        sa.Column("preco", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(["usuario"], ["usuarios.id"]),
        sa.PrimaryKeyConstraint("id")
    )

    # Tabela de itens dos pedidos
    op.create_table(
        "itens_pedidos",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("quantidade", sa.Integer(), nullable=True),
        sa.Column("sabor", sa.String(), nullable=True),
        sa.Column("tamanho", sa.String(), nullable=True),
        sa.Column("preco_unitario", sa.Float(), nullable=True),
        sa.Column("pedido", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["pedido"], ["pedidos.id"]),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade() -> None:
    """Desfaz a criação das tabelas."""

    op.drop_table("itens_pedidos")
    op.drop_table("pedidos")
    op.drop_table("usuarios")
