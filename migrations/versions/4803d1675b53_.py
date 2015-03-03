"""empty message

Revision ID: 4803d1675b53
Revises: 3914148d0cae
Create Date: 2015-03-02 21:28:01.995087

"""

# revision identifiers, used by Alembic.
revision = '4803d1675b53'
down_revision = '3914148d0cae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('num_attempts', sa.Integer(), nullable=False, server_default='0'))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'num_attempts')
    ### end Alembic commands ###
