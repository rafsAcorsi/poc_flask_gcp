"""create universe table

Revision ID: 2618f2ff5c8e
Revises: 729cc226555f
Create Date: 2019-04-10 18:18:36.748087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2618f2ff5c8e'
down_revision = '729cc226555f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Universe',
        sa.Column('id', sa.Integer()),
        sa.Column('name', sa.String(length=200), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table("Universe")
