"""add foreign key to post table

Revision ID: d5baf6dc00ac
Revises: 669797e1bc8e
Create Date: 2024-01-04 18:05:33.391577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5baf6dc00ac'
down_revision: Union[str, None] = '82760e4fb3e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.create_foreign_key('post_user_fk',source_table="posts",referent_table="user",local_cols=['owner_id'],
                          remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk',table_name='post')
    
    pass
