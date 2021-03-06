"""adding table

Revision ID: 5a76e1e601f0
Revises: 29b64fa26046
Create Date: 2020-03-03 21:30:25.279165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a76e1e601f0'
down_revision = '29b64fa26046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('processed_city',
    sa.Column('city', sa.String(length=140), nullable=False),
    sa.Column('keywords', sa.PickleType(), nullable=True),
    sa.Column('sentiment', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('city')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('processed_city')
    # ### end Alembic commands ###
