"""New database

Revision ID: 148def4e164b
Revises: dd12f10acbd9
Create Date: 2023-12-18 08:25:49.356791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '148def4e164b'
down_revision: Union[str, None] = 'dd12f10acbd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
