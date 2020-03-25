"""empty message

Revision ID: 115789827cfc
Revises: 9a6eeed156be
Create Date: 2020-03-24 06:52:57.745592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '115789827cfc'
down_revision = '9a6eeed156be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recommendation', 'hotel1')
    op.drop_column('recommendation', 'hotel2')
    op.drop_column('recommendation', 'flight2')
    op.drop_column('recommendation', 'key_attraction')
    op.drop_column('recommendation', 'flight1')
    op.drop_column('recommendation', 'county')
    op.drop_column('recommendation', 'hotel3')
    op.drop_column('recommendation', 'country')
    op.drop_column('recommendation', 'flight3')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recommendation', sa.Column('flight3', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('country', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('hotel3', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('county', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('flight1', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('key_attraction', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('flight2', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('hotel2', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('hotel1', sa.VARCHAR(length=140), nullable=True))
    # ### end Alembic commands ###
