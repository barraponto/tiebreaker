from components.create import create_review
from resources.repository import get_repository
from settings import Settings

settings = Settings()

repo = get_repository(settings)


"""
# The Tiebreaker Dashboard
"""

create_review(repo)
