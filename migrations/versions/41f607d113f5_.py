"""empty message

Revision ID: 41f607d113f5
Revises: 66db2a45b5ae
Create Date: 2018-11-02 16:33:10.837032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41f607d113f5'
down_revision = '66db2a45b5ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('registrs', sa.Column('index', sa.String(), nullable=True))
    op.drop_column('registrs', 'regtype_text')
    op.drop_column('registrs', 'atvk')
    op.drop_column('registrs', 'name_after_quotes')
    op.drop_column('registrs', 'name_in_quotes')
    op.drop_column('registrs', 'uri')
    op.drop_column('registrs', 'addressid')
    op.drop_column('registrs', 'without_quotes')
    op.drop_column('registrs', 'type_text')
    op.drop_column('registrs', 'name_before_quotes')
    op.drop_column('registrs', 'sepa')
    op.drop_column('registrs', 'regtype')
    op.drop_column('registrs', 'type')
    op.drop_column('registrs', 'reregistration_term')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('registrs', sa.Column('reregistration_term', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('type', sa.VARCHAR(length=3), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('regtype', sa.VARCHAR(length=1), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('sepa', sa.VARCHAR(length=18), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('name_before_quotes', sa.VARCHAR(length=254), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('type_text', sa.VARCHAR(length=60), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('without_quotes', sa.VARCHAR(length=254), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('addressid', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('uri', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('name_in_quotes', sa.VARCHAR(length=254), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('name_after_quotes', sa.VARCHAR(length=254), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('atvk', sa.VARCHAR(length=7), autoincrement=False, nullable=True))
    op.add_column('registrs', sa.Column('regtype_text', sa.VARCHAR(length=60), autoincrement=False, nullable=True))
    op.drop_column('registrs', 'index')
    # ### end Alembic commands ###
