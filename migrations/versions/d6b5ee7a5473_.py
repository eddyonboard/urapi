"""empty message

Revision ID: d6b5ee7a5473
Revises: 
Create Date: 2018-11-02 14:09:42.737082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6b5ee7a5473'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('registrs',
    sa.Column('regcode', sa.String(length=11), nullable=False),
    sa.Column('sepa', sa.String(length=18), nullable=True),
    sa.Column('name', sa.String(length=254), nullable=True),
    sa.Column('name_before_quotes', sa.String(length=254), nullable=True),
    sa.Column('name_in_quotes', sa.String(length=254), nullable=True),
    sa.Column('name_after_quotes', sa.String(length=254), nullable=True),
    sa.Column('without_quotes', sa.String(length=254), nullable=True),
    sa.Column('regtype', sa.String(length=1), nullable=True),
    sa.Column('regtype_text', sa.String(length=60), nullable=True),
    sa.Column('type', sa.String(length=3), nullable=True),
    sa.Column('type_text', sa.String(length=60), nullable=True),
    sa.Column('registered', sa.Date(), nullable=True),
    sa.Column('terminated', sa.Date(), nullable=True),
    sa.Column('closed', sa.String(length=1), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('addressid', sa.Integer(), nullable=True),
    sa.Column('region', sa.Integer(), nullable=True),
    sa.Column('city', sa.Integer(), nullable=True),
    sa.Column('atvk', sa.String(length=7), nullable=True),
    sa.Column('reregistration_term', sa.Date(), nullable=True),
    sa.Column('uri', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('regcode')
    )
    op.create_index(op.f('ix_registrs_regcode'), 'registrs', ['regcode'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_registrs_regcode'), table_name='registrs')
    op.drop_table('registrs')
    # ### end Alembic commands ###
