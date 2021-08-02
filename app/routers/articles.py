from app.schemas.articles import ArticleModel, ArticleDetailsModel, ArticleCreateModel
from app.schemas.authors import NoAuthorFoundByIDError
from app.utils import articles as articles_utils
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/articles/create", response_model=ArticleDetailsModel, status_code=201)
async def create_article(article: ArticleCreateModel):
    try:
        article = await articles_utils.create_article(article)
    except NoAuthorFoundByIDError as error:
        raise HTTPException(status_code=400, detail=error.message)

    return article


@router.get("/articles/get/{article_id}", response_model=ArticleDetailsModel)
async def get_article(article_id: int):
    return await articles_utils.get_article(article_id)


@router.get("/articles/get_by_author/{author_id}")
async def get_articles_by_author(author_id: int):
    articles = await articles_utils.get_articles_by_author(author_id)
    return {"results": articles}


@router.get("/articles/get_all")
async def get_articless():
    total_count = await articles_utils.get_articles_count()
    articles = await articles_utils.get_articles()
    return {"total_count": total_count, "results": articles}


@router.put("/articles/{article_id}", response_model=ArticleDetailsModel)
async def update_article(article_id: int, article_data: ArticleModel):
    await articles_utils.update_article(article_id=article_id, article=article_data)
    return await articles_utils.get_article(article_id)
