"""Add upload usage to port

Revision ID: 514f6e1b7a72
Revises: 0840e155743c
Create Date: 2020-11-17 04:18:36.261246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '514f6e1b7a72'
down_revision = '0840e155743c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('port', schema=None) as batch_op:
        batch_op.add_column(sa.Column('upload_usage', sa.Integer(), nullable=True))
    op.execute('UPDATE port set upload_usage=0')
    with op.batch_alter_table('port', schema=None) as batch_op:
        batch_op.alter_column('upload_usage', existing_type=sa.Integer(), nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('port', schema=None) as batch_op:
        batch_op.drop_column('upload_usage')

    # ### end Alembic commands ###
