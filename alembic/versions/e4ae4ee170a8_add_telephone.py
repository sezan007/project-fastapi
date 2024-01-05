"""add telephone

Revision ID: e4ae4ee170a8
Revises: 69399fba80a6
Create Date: 2024-01-05 14:04:15.791901

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4ae4ee170a8'
down_revision: Union[str, None] = '69399fba80a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_num', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_num')
    # ### end Alembic commands ###
