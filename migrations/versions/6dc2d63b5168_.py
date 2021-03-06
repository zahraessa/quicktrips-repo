"""empty message

Revision ID: 6dc2d63b5168
Revises: 115789827cfc
Create Date: 2020-03-24 06:59:51.514262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dc2d63b5168'
down_revision = '115789827cfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favourite', sa.Column('flights', sa.PickleType(), nullable=True))
    op.add_column('favourite', sa.Column('hotels', sa.PickleType(), nullable=True))
    op.add_column('favourite', sa.Column('image', sa.String(length=140), nullable=True))
    op.add_column('favourite', sa.Column('keywords', sa.PickleType(), nullable=True))
    op.drop_column('favourite', 'hotel3')
    op.drop_column('favourite', 'country')
    op.drop_column('favourite', 'flight3')
    op.drop_column('favourite', 'key_attraction')
    op.drop_column('favourite', 'hotel2')
    op.drop_column('favourite', 'hotel1')
    op.drop_column('favourite', 'flight1')
    op.drop_column('favourite', 'flight2')
    op.drop_column('recommendation', 'hotel3')
    op.drop_column('recommendation', 'country')
    op.drop_column('recommendation', 'flight3')
    op.drop_column('recommendation', 'key_attraction')
    op.drop_column('recommendation', 'hotel2')
    op.drop_column('recommendation', 'hotel1')
    op.drop_column('recommendation', 'county')
    op.drop_column('recommendation', 'flight1')
    op.drop_column('recommendation', 'flight2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recommendation', sa.Column('flight2', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('flight1', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('county', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('hotel1', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('hotel2', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('key_attraction', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('flight3', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('country', sa.VARCHAR(length=140), nullable=True))
    op.add_column('recommendation', sa.Column('hotel3', sa.VARCHAR(length=140), nullable=True))
    op.add_column('favourite', sa.Column('flight2', sa.VARCHAR(length=140), nullable=True))
    op.add_column('favourite', sa.Column('flight1', sa.VARCHAR(length=140), nullable=True))
    op.add_column('favourite', sa.Column('hotel1', sa.VARCHAR(length=140), nullable=True))
    op.add_column('favourite', sa.Column('hotel2', sa.VARCHAR(length=140), nullable=True))
    op.add_column('favourite', sa.Column('key_attraction', sa.VARCHAR(length=140), nullable=True))
    op.add_column('favourite', sa.Column('flight3', sa.VARCHAR(length=140), nullable=True))
    op.add_column('favourite', sa.Column('country', sa.VARCHAR(length=140), nullable=True))
    op.add_column('favourite', sa.Column('hotel3', sa.VARCHAR(length=140), nullable=True))
    op.drop_column('favourite', 'keywords')
    op.drop_column('favourite', 'image')
    op.drop_column('favourite', 'hotels')
    op.drop_column('favourite', 'flights')
    # ### end Alembic commands ###
