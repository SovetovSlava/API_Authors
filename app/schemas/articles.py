from pydantic import BaseModel


class ArticleModel(BaseModel):
    """ Validate request data """
    title: str
    content: str


class ArticleDetailsModel(ArticleModel):
    """ Return response data """
    id: int
    author_name: str


class ArticleCreateModel(ArticleModel):
    """ Return response data """
    author_id: int
