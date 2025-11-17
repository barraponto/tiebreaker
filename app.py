from agentic.composer import ReviewPost
from database.models import Game
from integrations.bgg import BoardGameGeek
from settings import Settings
from agentic.creator_chain import build_creator_chain


class App:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.bgg = BoardGameGeek()
        self.creator_chain = build_creator_chain()

    def generate_review(self, game: Game) -> ReviewPost:
        reviews = self.bgg.load_game_reviews(game.id)
        return self.creator_chain.invoke(
            [{"messages": [], "review": review} for review in reviews]
        )
