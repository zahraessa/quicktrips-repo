"""empty message

Revision ID: 7b9d48b0037f
Revises: f7d4fe5cf35e
Create Date: 2020-03-26 14:13:13.972101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b9d48b0037f'
down_revision = 'f7d4fe5cf35e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('current_recommendation', schema=None) as batch_op:
        batch_op.drop_column('image')

    with op.batch_alter_table('favourite', schema=None) as batch_op:
        batch_op.drop_column('image')

    with op.batch_alter_table('past_trip', schema=None) as batch_op:
        batch_op.drop_column('image')

    with op.batch_alter_table('processed_city', schema=None) as batch_op:
        batch_op.drop_column('image')

    with op.batch_alter_table('recommendation', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recommendation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=400), nullable=True))

    with op.batch_alter_table('processed_city', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=140), nullable=True))

    with op.batch_alter_table('past_trip', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=140), nullable=True))

    with op.batch_alter_table('favourite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=140), nullable=True))

    with op.batch_alter_table('current_recommendation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=140), nullable=True))

    # ### end Alembic commands ###
