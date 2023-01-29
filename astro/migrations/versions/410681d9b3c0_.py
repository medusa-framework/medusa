"""empty message

Revision ID: 410681d9b3c0
Revises: 1548f525b0ac
Create Date: 2023-01-28 04:26:28.870290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '410681d9b3c0'
down_revision = '1548f525b0ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uuid', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uuid', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('uuid')

    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('uuid')

    # ### end Alembic commands ###