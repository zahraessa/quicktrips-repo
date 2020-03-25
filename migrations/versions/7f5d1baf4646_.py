"""empty message

Revision ID: 7f5d1baf4646
Revises: 7836f82c1942
Create Date: 2020-03-23 14:50:26.141105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f5d1baf4646'
down_revision = '7836f82c1942'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('processed_city')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('processed_city',
    sa.Column('city', sa.VARCHAR(length=140), nullable=False),
    sa.Column('country', sa.VARCHAR(length=140), nullable=True),
    sa.Column('keywords', sa.BLOB(), nullable=True),
    sa.Column('sentiment', sa.FLOAT(), nullable=True),
    sa.Column('image', sa.VARCHAR(length=140), nullable=True),
    sa.Column('description', sa.VARCHAR(length=140), nullable=True),
    sa.PrimaryKeyConstraint('city')
    )
    # ### end Alembic commands ###
