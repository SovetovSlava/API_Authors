import sqlalchemy

metadata = sqlalchemy.MetaData()

authors_table = sqlalchemy.Table(
    "authors",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(100), nullable=False)
)
