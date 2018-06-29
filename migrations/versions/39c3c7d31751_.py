"""empty message

Revision ID: 39c3c7d31751
Revises: a1d616ded8b1
Create Date: 2018-06-28 19:13:34.960297

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '39c3c7d31751'
down_revision = 'a1d616ded8b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cm_user', 'cookies_vt',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('cm_user', 'ip_proxy_vt',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cm_user', 'ip_proxy_vt',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('cm_user', 'cookies_vt',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###