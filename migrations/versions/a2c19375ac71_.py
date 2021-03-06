"""empty message

Revision ID: a2c19375ac71
Revises: 0b4ebc1029c5
Create Date: 2020-03-31 09:50:34.971439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2c19375ac71'
down_revision = '0b4ebc1029c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shared_recommendations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Integer(), nullable=True),
    sa.Column('city', sa.String(length=140), nullable=True),
    sa.Column('description', sa.String(length=400), nullable=True),
    sa.Column('flights', sa.PickleType(), nullable=True),
    sa.Column('keywords', sa.PickleType(), nullable=True),
    sa.Column('hotels', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shared_recommendations')
    # ### end Alembic commands ###
