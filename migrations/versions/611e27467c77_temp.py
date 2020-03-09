"""temp

Revision ID: 611e27467c77
Revises: ec9bfce5fdf6
Create Date: 2020-03-08 16:27:45.751694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '611e27467c77'
down_revision = 'ec9bfce5fdf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities_to_avoid',
    sa.Column('city', sa.String(length=140), nullable=False),
    sa.PrimaryKeyConstraint('city')
    )
    op.create_table('processed_city',
    sa.Column('city', sa.String(length=140), nullable=False),
    sa.Column('country', sa.String(length=140), nullable=True),
    sa.Column('keywords', sa.PickleType(), nullable=True),
    sa.Column('sentiment', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('city')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('processed_city')
    op.drop_table('cities_to_avoid')
    # ### end Alembic commands ###
