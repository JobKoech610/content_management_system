"""New table relation btwn order and payment

Revision ID: 6ca773c7fd3f
Revises: d85fe2eb1814
Create Date: 2024-05-01 20:55:07.103712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ca773c7fd3f'
down_revision = 'd85fe2eb1814'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admins', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
        batch_op.alter_column('firstName',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('lastName',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.create_unique_constraint(None, ['email'])

    with op.batch_alter_table('communication_channels', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
        batch_op.alter_column('Message',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('publication_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('platform_id', sa.Integer(), nullable=True))
        batch_op.alter_column('Type',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('UnitPrice',
               existing_type=sa.VARCHAR(),
               type_=sa.Numeric(precision=10, scale=2),
               existing_nullable=True)
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.drop_constraint('orders_platformId_fkey', type_='foreignkey')
        batch_op.drop_constraint('orders_publicationId_fkey', type_='foreignkey')
        batch_op.drop_constraint('orders_userId_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'publications', ['publication_id'], ['id'])
        batch_op.create_foreign_key(None, 'platforms', ['platform_id'], ['id'])
        batch_op.drop_column('publicationId')
        batch_op.drop_column('platformId')
        batch_op.drop_column('userId')
        batch_op.drop_column('Date')

    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_id', sa.Integer(), nullable=True))
        batch_op.alter_column('Amount',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=10, scale=2),
               existing_nullable=True)
        batch_op.alter_column('referenceNo',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('paidVia',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.drop_constraint('payments_OrderId_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'orders', ['order_id'], ['id'])
        batch_op.drop_column('Date')
        batch_op.drop_column('OrderId')

    with op.batch_alter_table('platforms', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
        batch_op.alter_column('Publisher',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('Description',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('Image',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('Amount',
               existing_type=sa.VARCHAR(),
               type_=sa.Numeric(precision=10, scale=2),
               existing_nullable=True)

    with op.batch_alter_table('publications', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
        batch_op.alter_column('typeOfPublication',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.drop_constraint('publications_userId_fkey', type_='foreignkey')
        batch_op.drop_column('userId')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
        batch_op.alter_column('firstName',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('lastName',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('lastName',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('firstName',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('created_at')

    with op.batch_alter_table('publications', schema=None) as batch_op:
        batch_op.add_column(sa.Column('userId', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('publications_userId_fkey', 'users', ['userId'], ['id'])
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('typeOfPublication',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('created_at')

    with op.batch_alter_table('platforms', schema=None) as batch_op:
        batch_op.alter_column('Amount',
               existing_type=sa.Numeric(precision=10, scale=2),
               type_=sa.VARCHAR(),
               existing_nullable=True)
        batch_op.alter_column('Image',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('Description',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('Publisher',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('created_at')

    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('OrderId', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Date', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('payments_OrderId_fkey', 'orders', ['OrderId'], ['id'])
        batch_op.alter_column('paidVia',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('referenceNo',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('Amount',
               existing_type=sa.Numeric(precision=10, scale=2),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.drop_column('order_id')

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Date', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('userId', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('platformId', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('publicationId', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('orders_userId_fkey', 'users', ['userId'], ['id'])
        batch_op.create_foreign_key('orders_publicationId_fkey', 'publications', ['publicationId'], ['id'])
        batch_op.create_foreign_key('orders_platformId_fkey', 'platforms', ['platformId'], ['id'])
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('UnitPrice',
               existing_type=sa.Numeric(precision=10, scale=2),
               type_=sa.VARCHAR(),
               existing_nullable=True)
        batch_op.alter_column('Type',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('platform_id')
        batch_op.drop_column('user_id')
        batch_op.drop_column('publication_id')

    with op.batch_alter_table('communication_channels', schema=None) as batch_op:
        batch_op.alter_column('Message',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('created_at')

    with op.batch_alter_table('admins', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('lastName',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('firstName',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
