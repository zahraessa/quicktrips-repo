"""empty message

Revision ID: 94d692b43dce
Revises: 30ff260baddd
Create Date: 2020-03-23 14:49:28.951426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94d692b43dce'
down_revision = '30ff260baddd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('past_trip')
    op.add_column('recommendation', sa.Column('image', sa.String(length=400), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recommendation', 'image')
    op.create_table('past_trip',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('country', sa.VARCHAR(length=140), nullable=True),
    sa.Column('city', sa.VARCHAR(length=140), nullable=True),
    sa.Column('hotel1', sa.VARCHAR(length=140), nullable=True),
    sa.Column('flight1', sa.VARCHAR(length=140), nullable=True),
    sa.Column('hotel2', sa.VARCHAR(length=140), nullable=True),
    sa.Column('flight2', sa.VARCHAR(length=140), nullable=True),
    sa.Column('hotel3', sa.VARCHAR(length=140), nullable=True),
    sa.Column('flight3', sa.VARCHAR(length=140), nullable=True),
    sa.Column('key_attraction', sa.VARCHAR(length=140), nullable=True),
    sa.Column('description', sa.VARCHAR(length=400), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('image', sa.VARCHAR(length=140), nullable=True),
    sa.Column('region', sa.VARCHAR(length=140), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###