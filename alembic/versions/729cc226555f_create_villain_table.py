"""create villain table

Revision ID: 729cc226555f
Revises: 7a14cbd95cdd
Create Date: 2019-04-08 17:29:58.366262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '729cc226555f'
down_revision = '7a14cbd95cdd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Villain',
        sa.Column('id', sa.Integer()),
        sa.Column('name', sa.String(length=200), nullable=False),
        sa.Column('thumbnail_url', sa.String(length=200), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table("Villain")
