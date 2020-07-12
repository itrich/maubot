"""Add Matrix state store

Revision ID: 90aa88820eab
Revises: 4b93300852aa
Create Date: 2020-07-12 01:50:06.215623

"""
from alembic import op
import sqlalchemy as sa

from mautrix.client.state_store.sqlalchemy import SerializableType
from mautrix.types import PowerLevelStateEventContent, RoomEncryptionStateEventContent


# revision identifiers, used by Alembic.
revision = '90aa88820eab'
down_revision = '4b93300852aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mx_room_state',
    sa.Column('room_id', sa.String(length=255), nullable=False),
    sa.Column('is_encrypted', sa.Boolean(), nullable=True),
    sa.Column('has_full_member_list', sa.Boolean(), nullable=True),
    sa.Column('encryption', SerializableType(RoomEncryptionStateEventContent), nullable=True),
    sa.Column('power_levels', SerializableType(PowerLevelStateEventContent), nullable=True),
    sa.PrimaryKeyConstraint('room_id')
    )
    op.create_table('mx_user_profile',
    sa.Column('room_id', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.String(length=255), nullable=False),
    sa.Column('membership', sa.Enum('JOIN', 'LEAVE', 'INVITE', 'BAN', 'KNOCK', name='membership'), nullable=False),
    sa.Column('displayname', sa.String(), nullable=True),
    sa.Column('avatar_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('room_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mx_user_profile')
    op.drop_table('mx_room_state')
    # ### end Alembic commands ###
