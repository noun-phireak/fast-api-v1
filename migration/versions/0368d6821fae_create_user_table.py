"""Create user table

Revision ID: 0368d6821fae
Revises: 69b1e2161492
Create Date: 2023-03-08 22:29:47.920502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0368d6821fae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('name', sa.String(16), nullable=False),
                    sa.Column('type_id',sa.Integer(), nullable=True),
                    sa.Column('email',sa.String(20), nullable=True),
                    sa.Column('password',sa.String(150), nullable=False)
                    )

def downgrade() -> None:
    op.drop_table('users')
