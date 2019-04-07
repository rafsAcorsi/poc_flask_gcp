"""create contact table

Revision ID: a242eb1145f9
Revises: 
Create Date: 2019-04-01 14:13:39.601313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a242eb1145f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Hero',
        sa.Column('id', sa.Integer()),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('birthday', sa.DateTime()),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table("account")
