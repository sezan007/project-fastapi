"""add content column to post table

Revision ID: f7e6778dc407
Revises: af4d6a69eccb
Create Date: 2024-01-04 15:48:08.612651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7e6778dc407'
down_revision: Union[str, None] = 'af4d6a69eccb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
