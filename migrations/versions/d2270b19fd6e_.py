"""empty message

Revision ID: d2270b19fd6e
Revises: d36b420ea928
Create Date: 2023-09-14 08:56:09.442153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2270b19fd6e'
down_revision = 'd36b420ea928'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('invoice', schema=None) as batch_op:
        batch_op.add_column(sa.Column('due_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('client', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_invoice_client', 'client', ['client'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('invoice', schema=None) as batch_op:
        batch_op.drop_constraint('fk_invoice_client', type_='foreignkey')
        batch_op.drop_column('client')
        batch_op.drop_column('due_date')

    # ### end Alembic commands ###