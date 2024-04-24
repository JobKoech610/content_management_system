"""tables

Revision ID: 57b39139c452
Revises: 86125298d298
Create Date: 2024-04-21 19:37:19.258128

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '57b39139c452'
down_revision = '86125298d298'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'admins',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('firstName', sa.String(length=100), nullable=False),
        sa.Column('lastName', sa.String(length=200), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('password', sa.String(length=500), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now()),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('firstName', sa.String(length=100), nullable=False),
        sa.Column('lastName', sa.String(length=200), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('password', sa.String(length=500), nullable=False),
        sa.Column('status', sa.String(length=200), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now()),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    op.create_table(
        'platforms',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('Publisher', sa.String(length=100), nullable=False),
        sa.Column('Description', sa.String(length=1000), nullable=False),
        sa.Column('Image', sa.String(length=500), nullable=False),
        sa.Column('Amount', sa.Numeric(10, 2)),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now()),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'publications',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('typeOfPublication', sa.String(length=100), nullable=False),
        sa.Column('status', sa.String(length=200), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now()),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'communication_channels',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('Message', sa.String(length=1000), nullable=False),
        sa.Column('user_id', sa.Integer()),
        sa.Column('admin_id', sa.Integer()),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now()),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('Type', sa.String(length=100), nullable=False),
        sa.Column('UnitPrice', sa.Numeric(10, 2)),
        sa.Column('status', sa.String(length=200), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('platform_id', sa.Integer(), sa.ForeignKey('platforms.id')),
        sa.Column('publication_id', sa.Integer(), sa.ForeignKey('publications.id')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now()),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'payments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('Amount', sa.Numeric(10, 2)),
        sa.Column('referenceNo', sa.Integer(), nullable=False),
        sa.Column('paidVia', sa.String(length=100), nullable=False),
        sa.Column('order_id', sa.Integer(), sa.ForeignKey('orders.id')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now()),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    pass

