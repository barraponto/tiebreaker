from components.create import create_review
from resources.app import get_app
from resources.repository import get_repository
from settings import Settings

settings = Settings()

app = get_app(settings)
repo = get_repository(settings)

"""
# The Tiebreaker Dashboard
"""

create_review(repo, app)
