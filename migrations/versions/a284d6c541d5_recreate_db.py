"""recreate db

Revision ID: a284d6c541d5
Revises: 
Create Date: 2021-02-18 21:54:43.801171

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a284d6c541d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jobs',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('initialization_date', sa.DateTime(), nullable=True),
    sa.Column('finish_date', sa.DateTime(), nullable=True),
    sa.Column('currently_working', sa.Boolean(), nullable=True),
    sa.Column('company', sa.String(length=50), nullable=False),
    sa.Column('position', sa.String(length=50), nullable=False),
    sa.Column('freelance', sa.Boolean(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_jobs_id'), 'jobs', ['id'], unique=True)
    op.create_table('employee',
    sa.Column('jobs_id', postgresql.UUID(), nullable=False),
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('first_name', sa.String(length=16), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('confirm_email', sa.Boolean(), nullable=True),
    sa.Column('country', sa.String(length=25), nullable=False),
    sa.Column('city', sa.String(length=40), nullable=False),
    sa.Column('website', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['jobs_id'], ['jobs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_id'), 'employee', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employee_id'), table_name='employee')
    op.drop_table('employee')
    op.drop_index(op.f('ix_jobs_id'), table_name='jobs')
    op.drop_table('jobs')
    # ### end Alembic commands ###
