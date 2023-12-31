"""add a phone number to user

Revision ID: a1831665bcf9
Revises: 
Create Date: 2023-11-08 20:43:57.768713

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1831665bcf9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(20),nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
