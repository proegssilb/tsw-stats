"""Create some indexes.

Revision ID: 7508e6ddea8d
Revises:
Create Date: 2017-01-31 14:44:46.595003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7508e6ddea8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_attacktype_table_encid'), 'attacktype_table', ['encid'], unique=False)
    op.create_index(op.f('ix_attacktype_table_starttime'), 'attacktype_table', ['starttime'], unique=False)
    op.create_index(op.f('ix_combatant_table_encid'), 'combatant_table', ['encid'], unique=False)
    op.create_index(op.f('ix_combatant_table_name'), 'combatant_table', ['name'], unique=False)
    op.add_column('current_table', sa.Column('currentid', sa.BigInteger(), nullable=False, primary_key=True))
    op.create_index(op.f('ix_damagetype_table_combatant'), 'damagetype_table', ['combatant'], unique=False)
    op.create_index(op.f('ix_damagetype_table_encid'), 'damagetype_table', ['encid'], unique=False)
    op.create_index(op.f('ix_encounter_table_endtime'), 'encounter_table', ['endtime'], unique=False)
    op.create_index('idx_swing_encid_attacker', 'swing_table', ['encid', 'attacker'], unique=False)
    op.create_index(op.f('ix_swing_table_stime'), 'swing_table', ['stime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_swing_table_stime'), table_name='swing_table')
    op.drop_index('idx_swing_encid_attacker', table_name='swing_table')
    op.drop_index(op.f('ix_encounter_table_endtime'), table_name='encounter_table')
    op.drop_index(op.f('ix_damagetype_table_encid'), table_name='damagetype_table')
    op.drop_index(op.f('ix_damagetype_table_combatant'), table_name='damagetype_table')
    op.drop_column('current_table', 'currentid')
    op.drop_index(op.f('ix_combatant_table_name'), table_name='combatant_table')
    op.drop_index(op.f('ix_combatant_table_encid'), table_name='combatant_table')
    op.drop_index(op.f('ix_attacktype_table_starttime'), table_name='attacktype_table')
    op.drop_index(op.f('ix_attacktype_table_encid'), table_name='attacktype_table')
    # ### end Alembic commands ###