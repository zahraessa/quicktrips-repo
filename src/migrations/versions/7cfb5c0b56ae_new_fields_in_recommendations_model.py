"""new fields in recommendations model

Revision ID: 7cfb5c0b56ae
Revises: 265949a3941d
Create Date: 2020-01-11 23:03:39.011576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cfb5c0b56ae'
down_revision = '265949a3941d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recommendation', sa.Column('key_attraction', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recommendation', 'key_attraction')
    # ### end Alembic commands ###
