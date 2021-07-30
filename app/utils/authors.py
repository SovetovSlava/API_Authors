from app.models.database import database
from app.models.authors import authors_table
from app.schemas import authors as author_schema
from sqlalchemy import select


async def get_author(author_id: int):
    query = authors_table.select().where(authors_table.c.id == author_id)
    return await database.fetch_one(query)


async def get_author_by_name(name: str):
    query = authors_table.select().where(authors_table.c.name == name)
    return await database.fetch_one(query)


async def get_authors():
    query = (
        select(
            [
                authors_table.c.id,
                authors_table.c.name,
            ]
        )
    )
    return await database.fetch_all(query)


async def create_author(author: author_schema.AuthorBase):
    query = (
        authors_table.insert()
            .values(
            name=author.name
        )
            .returning(
            authors_table.c.id,
            authors_table.c.name,
        )
    )

    author = await database.fetch_one(query)
    return author


async def update_author(author_id: int, author: author_schema.AuthorBase):
    query = (
        authors_table.update()
            .where(authors_table.c.id == author_id)
            .values(name=author.name)
    )
    return await database.execute(query)