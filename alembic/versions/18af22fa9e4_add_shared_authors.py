"""Add shared authors

Revision ID: 18af22fa9e4
Revises: 3afc6d6bfd9
Create Date: 2014-09-06 21:04:36.181385

"""

# revision identifiers, used by Alembic.
revision = '18af22fa9e4'
down_revision = '3afc6d6bfd9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sharedauthor', sa.Column('accepted', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sharedauthor', 'accepted')
    ### end Alembic commands ###
