"""empty message

Revision ID: 7de42cf6ce0e
Revises: 0338cbc9da71
Create Date: 2019-03-02 02:06:02.866880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7de42cf6ce0e'
down_revision = '0338cbc9da71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('country', sa.String(length=32), nullable=True),
    sa.Column('remark', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_author_country'), 'author', ['country'], unique=False)
    op.create_index(op.f('ix_author_name'), 'author', ['name'], unique=False)
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_name'), 'category', ['name'], unique=False)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('file', sa.String(length=64), nullable=False),
    sa.Column('cover_img', sa.Text(), nullable=True),
    sa.Column('upload_time', sa.DateTime(), nullable=True),
    sa.Column('creater_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['creater_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('file')
    )
    op.create_index(op.f('ix_book_name'), 'book', ['name'], unique=False)
    op.create_table('author_book',
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('author_id', 'book_id')
    )
    op.create_table('category_book',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('category_id', 'book_id')
    )
    op.add_column('posts', sa.Column('draft', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'draft')
    op.drop_table('category_book')
    op.drop_table('author_book')
    op.drop_index(op.f('ix_book_name'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_category_name'), table_name='category')
    op.drop_table('category')
    op.drop_index(op.f('ix_author_name'), table_name='author')
    op.drop_index(op.f('ix_author_country'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###
