"""migrate

Revision ID: d85fe2eb1814
Revises: 762435d6de73
Create Date: 2024-05-01 15:34:38.807360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd85fe2eb1814'
down_revision = '762435d6de73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))

    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
