"""empty message

Revision ID: fbc05fd6722e
Revises: 1d1426b47ac9
Create Date: 2020-03-24 09:33:32.597056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbc05fd6722e'
down_revision = '1d1426b47ac9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('past_trip', 'region')
    op.drop_column('past_trip', 'city')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('past_trip', sa.Column('city', sa.VARCHAR(length=140), nullable=True))
    op.add_column('past_trip', sa.Column('region', sa.VARCHAR(length=140), nullable=True))
    # ### end Alembic commands ###