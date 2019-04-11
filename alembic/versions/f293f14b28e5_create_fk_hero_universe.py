"""create fk hero universe

Revision ID: f293f14b28e5
Revises: 2618f2ff5c8e
Create Date: 2019-04-10 18:19:01.858320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f293f14b28e5'
down_revision = '2618f2ff5c8e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'Hero',
        sa.Column('universe_id', sa.Integer())
    )
    op.create_foreign_key(
        'fk_universe_hero',
        'Hero', 'Universe',
        ['universe_id'], ['id'],
    )


def downgrade():
    op.drop_constraint('fk_universe_hero', 'Hero', type_='foreignkey')
    op.drop_column('Hero', 'universe_id')
