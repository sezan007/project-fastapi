"""add last few comulmns to post table

Revision ID: fb82c8a965b0
Revises: d5baf6dc00ac
Create Date: 2024-01-05 13:30:24.807028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb82c8a965b0'
down_revision: Union[str, None] = 'd5baf6dc00ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(),nullable=False,server_default=sa.text('now()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
