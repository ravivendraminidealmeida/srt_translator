"""empty message

Revision ID: eb57c9bc0f95
Revises: 
Create Date: 2025-07-21 17:00:19.794434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb57c9bc0f95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('filename', sa.String(), nullable=True),
    sa.Column('from_lang', sa.String(), nullable=True),
    sa.Column('to_lang', sa.String(), nullable=True),
    sa.Column('original_storage_ref', sa.String(), nullable=True),
    sa.Column('translated_storage_ref', sa.String(), nullable=True),
    sa.Column('download_link', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translation')
    op.drop_table('user')
    # ### end Alembic commands ###
