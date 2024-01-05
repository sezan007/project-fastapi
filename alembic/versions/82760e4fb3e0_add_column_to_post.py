"""add column to post

Revision ID: 82760e4fb3e0
Revises: d5baf6dc00ac
Create Date: 2024-01-05 12:49:01.705002

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82760e4fb3e0'
down_revision: Union[str, None] = '669797e1bc8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    #op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','owner_id')
    pass
