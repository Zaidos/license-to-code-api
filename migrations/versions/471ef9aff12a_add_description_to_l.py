"""add description to licenses

Revision ID: 471ef9aff12a
Revises: 3c5e5f35b467
Create Date: 2012-12-13 22:59:59.644199

"""

# revision identifiers, used by Alembic.
revision = '471ef9aff12a'
down_revision = '3c5e5f35b467'

from alembic import op
import sqlalchemy as sa


def upgrade():
  op.add_column('licenses', sa.Column('description', sa.Text))

def downgrade():
  op.drop_column('licenses', 'description')
