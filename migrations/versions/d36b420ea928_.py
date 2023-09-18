"""empty message

Revision ID: d36b420ea928
Revises: 1d9a51a3fdc5
Create Date: 2023-09-14 08:33:55.778583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd36b420ea928'
down_revision = '1d9a51a3fdc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('invoice', schema=None) as batch_op:
        batch_op.drop_column('due_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('invoice', schema=None) as batch_op:
        batch_op.add_column(sa.Column('due_date', sa.DATE(), nullable=False))

    # ### end Alembic commands ###
