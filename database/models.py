from pydantic import BaseModel


class Game(BaseModel):
    id: int
    yearpublished: int
    name: str
