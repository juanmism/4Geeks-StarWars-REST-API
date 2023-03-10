"""empty message

Revision ID: 4205714a2f76
Revises: 3aebacf17d70
Create Date: 2023-01-22 08:46:39.614705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4205714a2f76'
down_revision = '3aebacf17d70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('hair', sa.String(length=250), nullable=True),
    sa.Column('eyes', sa.String(length=250), nullable=True),
    sa.Column('birth', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('favorite_user_id', sa.Integer(), nullable=True),
    sa.Column('favorite_people_id', sa.Integer(), nullable=True),
    sa.Column('favorite_planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['favorite_planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['favorite_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    op.drop_table('people')
    # ### end Alembic commands ###
