"""add user_id to tasks

Revision ID: 40073df74e1b
Revises: 
Create Date: 2026-10-15 12:35:22.949257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40073df74e1b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add user_id as nullable temporarily
    op.add_column(
        'user_tasks',
        sa.Column('user_id', sa.Integer(), nullable=True)
    )

    # Assign existing tasks to an existing user
    op.execute(
        "UPDATE user_tasks SET user_id = 1 WHERE user_id IS NULL"
    )

    # Make user_id mandatory
    op.alter_column(
        'user_tasks',
        'user_id',
        existing_type=sa.Integer(),
        nullable=False
    )

    # Add foreign key to the user table
    op.create_foreign_key(
        'fk_user_tasks_user_id',
        'user_tasks',
        'user_table',
        ['user_id'],
        ['id']
    )


def downgrade() -> None:
    op.drop_constraint(
        'fk_user_tasks_user_id',
        'user_tasks',
        type_='foreignkey'
    )
    op.drop_column('user_tasks', 'user_id')
