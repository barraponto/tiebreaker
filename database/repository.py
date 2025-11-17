from sqlalchemy import Engine
from sqlalchemy.sql import select, func
from database.engine import get_engine
from database.models import Game
from database.tables import games
from settings import Settings


class Repository:
    def __init__(self, settings: Settings):
        self.engine: Engine = get_engine(settings.database_url)

    def find_game_by_name(self, name: str) -> list[Game]:
        statement = (
            select(games).where(func.lower(games.c.name).contains(name)).limit(10)
        )

        with self.engine.connect() as connection:
            return [Game(**row) for row in connection.execute(statement).mappings()]
