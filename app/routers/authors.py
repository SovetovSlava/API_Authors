from app.utils import authors as authors_utils
from app.schemas.authors import AuthorBase, AuthorDetailsModel
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def health_check():
    return {"Hello": "World"}


@router.post("/authors/create", response_model=AuthorDetailsModel, status_code=201)
async def create_author(author: AuthorBase):
    author = await authors_utils.create_author(author)
    return author


@router.get("/authors/get/{author_id}", response_model=AuthorDetailsModel)
async def get_author(author_id: int):
    return await authors_utils.get_author(author_id)


@router.get("/authors/get_all")
async def get_authors():
    authors = await authors_utils.get_authors()
    return authors


@router.put("/authors/{author_id}", response_model=AuthorDetailsModel)
async def update_author(author_id: int, author_data: AuthorBase):
    await authors_utils.update_author(author_id=author_id, author=author_data)
    return await authors_utils.get_author(author_id)
