"""cities table

Revision ID: 6201f84348b3
Revises: 64fd9a43a1a2
Create Date: 2020-03-03 09:31:01.293441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6201f84348b3'
down_revision = '64fd9a43a1a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('processed_city',
    sa.Column('city', sa.String(length=140), nullable=False),
    sa.Column('keywords', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('sentiment', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('city')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('processed_city')
    # ### end Alembic commands ###
