"""empty message

Revision ID: db1f8e640b8a
Revises: 192f06a168f8
Create Date: 2020-07-17 18:09:08.603621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db1f8e640b8a'
down_revision = '192f06a168f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('storage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=64), nullable=True),
    sa.Column('path', sa.Unicode(length=128), nullable=True),
    sa.Column('type', sa.Unicode(length=3), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('storage')
    # ### end Alembic commands ###