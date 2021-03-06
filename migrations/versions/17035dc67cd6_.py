"""empty message

Revision ID: 17035dc67cd6
Revises: f9bb74332505
Create Date: 2020-03-28 00:40:36.778679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17035dc67cd6'
down_revision = 'f9bb74332505'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favourite', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_favourite_city'), ['city'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favourite', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_favourite_city'))

    # ### end Alembic commands ###
