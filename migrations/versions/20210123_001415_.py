"""empty message

Revision ID: 6bf2424518b1
Revises: ffdc0a98111c
Create Date: 2021-01-23 00:14:15.951354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bf2424518b1'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('album', sa.String(length=255), nullable=False),
    sa.Column('lyrics', sa.Text(), nullable=False),
    sa.Column('song_url', sa.Text(), nullable=False),
    sa.Column('media_url', sa.Text(), nullable=True),
    sa.Column('user_Id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_Id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('annotations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_facts', sa.Text(), nullable=False),
    sa.Column('user_Id', sa.Integer(), nullable=False),
    sa.Column('song_Id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['song_Id'], ['songs.id'], ),
    sa.ForeignKeyConstraint(['user_Id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_comment', sa.Text(), nullable=False),
    sa.Column('user_Id', sa.Integer(), nullable=False),
    sa.Column('song_Id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['song_Id'], ['songs.id'], ),
    sa.ForeignKeyConstraint(['user_Id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('votes', sa.Integer(), nullable=False),
    sa.Column('user_Id', sa.Integer(), nullable=False),
    sa.Column('song_Id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['song_Id'], ['songs.id'], ),
    sa.ForeignKeyConstraint(['user_Id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    op.drop_table('comments')
    op.drop_table('annotations')
    op.drop_table('songs')
    # ### end Alembic commands ###
