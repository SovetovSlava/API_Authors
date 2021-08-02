from app.models.database import database
from app.models.articles import articles_table
from app.models.authors import authors_table
from app.schemas import articles as article_schema
from app.schemas import authors as author_schema
from app.utils import authors as authors_utils
from sqlalchemy import func, select


async def create_article(article: article_schema.ArticleCreateModel):

    author = await authors_utils.get_author(article.author_id)

    if author is None:
        return author_schema.NoAuthorFoundByIDError(article.author_id)

    query = (
        articles_table.insert()
            .values(
            title=article.title,
            content=article.content,
            author_id=author["id"],
        )
            .returning(
            articles_table.c.id,
            articles_table.c.title,
            articles_table.c.content,
        )
    )
    article = await database.fetch_one(query)

    # Convert to dict and add author_name key to it
    article = dict(zip(article, article.values()))
    article["author_name"] = author["name"]
    return article


async def get_article(article_id: int):
    query = (
        select(
            [
                articles_table.c.id,
                articles_table.c.title,
                articles_table.c.content,
                articles_table.c.author_id,
                authors_table.c.name.label("author_name"),
            ]
        )
            .select_from(articles_table.join(authors_table))
            .where(articles_table.c.id == article_id)
    )
    return await database.fetch_one(query)


async def get_articles_by_author(author_id: int):
    query = (
        select(
            [
                articles_table.c.id,
                articles_table.c.title,
                articles_table.c.content,
                articles_table.c.author_id,
                authors_table.c.name.label("author_name"),
            ]
        )
            .select_from(articles_table.join(authors_table))
            .where(articles_table.c.author_id == author_id)
    )
    return await database.fetch_all(query)


async def get_articles():
    query = (
        select(
            [
                articles_table.c.id,
                articles_table.c.title,
                articles_table.c.content,
                articles_table.c.author_id,
                authors_table.c.name.label("author_name"),
            ]
        )
            .select_from(articles_table.join(authors_table))
    )
    return await database.fetch_all(query)


async def get_articles_count():
    query = select([func.count()]).select_from(articles_table)
    return await database.fetch_val(query)


async def update_article(article_id: int, article: article_schema.ArticleModel):
    query = (
        articles_table.update()
            .where(articles_table.c.id == article_id)
            .values(title=article.title, content=article.content)
    )
    return await database.execute(query)
