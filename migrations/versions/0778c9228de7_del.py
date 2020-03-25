"""del

Revision ID: 0778c9228de7
Revises: 4f3ca8f72b79
Create Date: 2020-03-23 14:45:10.231320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0778c9228de7'
down_revision = '4f3ca8f72b79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('processed_city')
    op.add_column('past_trip', sa.Column('image', sa.String(length=140), nullable=True))
    op.add_column('past_trip', sa.Column('region', sa.String(length=140), nullable=True))
    op.drop_column('past_trip', 'flight3')
    op.drop_column('past_trip', 'flight2')
    op.drop_column('past_trip', 'hotel2')
    op.drop_column('past_trip', 'description')
    op.drop_column('past_trip', 'hotel1')
    op.drop_column('past_trip', 'hotel3')
    op.drop_column('past_trip', 'flight1')
    op.drop_column('past_trip', 'key_attraction')
    op.add_column('recommendation', sa.Column('image', sa.String(length=400), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recommendation', 'image')
    op.add_column('past_trip', sa.Column('key_attraction', sa.VARCHAR(length=140), nullable=True))
    op.add_column('past_trip', sa.Column('flight1', sa.VARCHAR(length=140), nullable=True))
    op.add_column('past_trip', sa.Column('hotel3', sa.VARCHAR(length=140), nullable=True))
    op.add_column('past_trip', sa.Column('hotel1', sa.VARCHAR(length=140), nullable=True))
    op.add_column('past_trip', sa.Column('description', sa.VARCHAR(length=400), nullable=True))
    op.add_column('past_trip', sa.Column('hotel2', sa.VARCHAR(length=140), nullable=True))
    op.add_column('past_trip', sa.Column('flight2', sa.VARCHAR(length=140), nullable=True))
    op.add_column('past_trip', sa.Column('flight3', sa.VARCHAR(length=140), nullable=True))
    op.drop_column('past_trip', 'region')
    op.drop_column('past_trip', 'image')
    op.create_table('processed_city',
    sa.Column('city', sa.VARCHAR(length=140), nullable=False),
    sa.Column('country', sa.VARCHAR(length=140), nullable=True),
    sa.Column('keywords', sa.BLOB(), nullable=True),
    sa.Column('sentiment', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('city')
    )
    # ### end Alembic commands ###
