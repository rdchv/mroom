"""empty message

Revision ID: 62a1adaafa1a
Revises: 66917a424b1a
Create Date: 2020-06-30 11:53:41.881890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62a1adaafa1a'
down_revision = '66917a424b1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.Integer(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('rating_stars_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['rating_stars_id'], ['rating_stars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rating')
    # ### end Alembic commands ###