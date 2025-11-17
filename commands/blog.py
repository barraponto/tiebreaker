from pathlib import Path
from plumbum import local
from database.models import Game
from agentic.composer import ReviewPost

content_path = Path("blog/posts")


def generate_post(game: Game, post: ReviewPost):
    local.cmd.just("generate-post", str(game.id), post.title)
    with open(content_path / f"{game.id}.md", "a") as post_file:
        post_file.write(f"# {post.title}\n\n{post.body}")
    local.cmd.just("generate-blog")
