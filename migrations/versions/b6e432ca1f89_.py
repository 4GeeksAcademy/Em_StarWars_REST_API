"""empty message

Revision ID: b6e432ca1f89
Revises: 86e073e1f201
Create Date: 2023-12-21 11:01:36.195354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6e432ca1f89'
down_revision = '86e073e1f201'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('favorites',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('favorites',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)

    # ### end Alembic commands ###