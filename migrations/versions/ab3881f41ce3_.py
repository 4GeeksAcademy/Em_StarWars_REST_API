"""empty message

Revision ID: ab3881f41ce3
Revises: a6309a08dd3a
Create Date: 2023-12-17 09:59:17.833265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab3881f41ce3'
down_revision = 'a6309a08dd3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('species', sa.String(length=80), nullable=False),
    sa.Column('height', sa.String(length=120), nullable=False),
    sa.Column('eye_color', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('characters')
    # ### end Alembic commands ###
