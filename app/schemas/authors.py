from pydantic import BaseModel


class AuthorBase(BaseModel):
    """ Return response data """
    name: str


class AuthorDetailsModel(AuthorBase):
    """ Return response data """
    id: int
