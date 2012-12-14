"""create license table

Revision ID: 3c5e5f35b467
Revises: None
Create Date: 2012-12-13 18:47:14.688834

"""

# revision identifiers, used by Alembic.
revision = '3c5e5f35b467'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
  op.create_table(
    'licenses',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(256), nullable=False),
    sa.Column('abbv', sa.String(25), nullable=True),
    sa.Column('version', sa.String(128))
  )

def downgrade():
  op.drop_table('licenses')
