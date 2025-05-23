"""Created relationships in User, Post and Comment

Revision ID: d57fce153777
Revises: ddc718a0af1c
Create Date: 2025-05-15 18:47:13.406523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd57fce153777'
down_revision: Union[str, None] = 'ddc718a0af1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('uid', sa.Uuid(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('post_id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.uid'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.uid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_index(op.f('ix_comments_uid'), 'comments', ['uid'], unique=False)
    op.add_column('posts', sa.Column('user_id', sa.Uuid(), nullable=False))
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['uid'], ondelete='CASCADE')
    op.drop_column('posts', 'owner')
    # op.add_column('users', sa.Column('uid', sa.Uuid(), nullable=False)) -> Renamed the column manually instead as Alembic is incapable of renaming stuff
    op.alter_column('users', 'first_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'last_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'age',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('users', 'bio',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'deleted',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('users', 'pg_16',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('users', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.create_index(op.f('ix_users_uid'), 'users', ['uid'], unique=False)
    # op.drop_column('users', 'id') -> Same reason as line 37
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('id', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_users_uid'), table_name='users')
    op.alter_column('users', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('users', 'pg_16',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('users', 'deleted',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('users', 'bio',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'age',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('users', 'last_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'first_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('users', 'uid')
    op.add_column('posts', sa.Column('owner', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    op.drop_index(op.f('ix_comments_uid'), table_name='comments')
    op.drop_table('comments')
    # ### end Alembic commands ###
