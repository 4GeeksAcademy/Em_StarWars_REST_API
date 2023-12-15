"""empty message

Revision ID: 6fcc7afac046
Revises: 1d9adcd77169
Create Date: 2023-12-15 19:27:37.632040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fcc7afac046'
down_revision = '1d9adcd77169'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('Username',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=120),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('Username',
               existing_type=sa.String(length=120),
               type_=sa.BOOLEAN(),
               existing_nullable=False)

    # ### end Alembic commands ###
