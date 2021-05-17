"""notes table

Revision ID: 55571a35f79c
Revises: f02aa400515f
Create Date: 2021-05-17 08:35:49.824338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55571a35f79c'
down_revision = 'f02aa400515f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transfer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['transfer_id'], ['transfer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('notes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('transfer_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['transfer_id'], ['transfer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('note')
    # ### end Alembic commands ###
