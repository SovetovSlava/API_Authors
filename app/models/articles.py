import sqlalchemy

from .authors import authors_table

metadata = sqlalchemy.MetaData()

articles_table = sqlalchemy.Table(
    "articles",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("author_id", sqlalchemy.ForeignKey(authors_table.c.id)),
    sqlalchemy.Column("content", sqlalchemy.Text()),
    sqlalchemy.Column("title", sqlalchemy.String(100)),
)
