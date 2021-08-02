from pydantic import BaseModel


class AuthorBase(BaseModel):
    """ Return response data """
    name: str


class AuthorDetailsModel(AuthorBase):
    """ Return response data """
    id: int


class NoAuthorFoundByIDError(Exception):
    def __init__(self, id):
        self.message = f'Incorrect author_id: {id}'
