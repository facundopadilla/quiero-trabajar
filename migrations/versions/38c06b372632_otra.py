"""otra

Revision ID: 38c06b372632
Revises: 618b1de1cacc
Create Date: 2021-02-18 22:31:16.164481

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '38c06b372632'
down_revision = '618b1de1cacc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('jobs_id', postgresql.UUID(), nullable=True))
    op.create_foreign_key(None, 'employee', 'jobs', ['jobs_id'], ['employee_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employee', type_='foreignkey')
    op.drop_column('employee', 'jobs_id')
    # ### end Alembic commands ###