"""create hero table

Revision ID: 7a14cbd95cdd
Revises: 
Create Date: 2019-04-07 18:28:03.460153

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7a14cbd95cdd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Hero',
        sa.Column('id', sa.Integer()),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('thumbnail_url', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table("Hero")
