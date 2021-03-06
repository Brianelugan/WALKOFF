"""0.9.0

Revision ID: e2823c35d85c
Revises: 8a602ed5ea63
Create Date: 2018-11-19 16:19:32.509524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2823c35d85c'
down_revision = '8a602ed5ea63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('case_subscription')
    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_role_name'), ['name'])

    with op.batch_alter_table('scheduled_workflow', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_scheduled_workflow_task_id_scheduled_task'), 'scheduled_task', ['task_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')

    with op.batch_alter_table('scheduled_workflow', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_scheduled_workflow_task_id_scheduled_task'), type_='foreignkey')
        batch_op.create_foreign_key(None, 'scheduled_task', ['task_id'], ['id'])

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_role_name'), type_='unique')

    op.create_table('case_subscription',
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('modified_at', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('subscriptions', sa.TEXT(), nullable=True),
    sa.Column('note', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
