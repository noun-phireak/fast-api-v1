"""create user type table

Revision ID: a0559962e2fb
Revises: 0368d6821fae
Create Date: 2023-03-10 23:54:18.579061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0559962e2fb'
down_revision = '0368d6821fae'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('type',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('name', sa.String(16), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('type')
