import httpx
from pydantic import BaseModel


class BGGThread(BaseModel):
    id: str
    subject: str


class BGGComment(BaseModel):
    id: str
    canonical_link: str
    body: str


class BoardGameGeek:
    def __init__(self):
        self.client = httpx.Client(base_url="https://api.geekdo.com")

    def get_bgg_threads(self, game_id: int) -> list[BGGThread]:
        response = self.client.get(
            "/api/forums/threads",
            params={
                "forumid": 63,
                "nosession": 1,
                "objectid": game_id,
                "objecttype": "thing",
                "pageid": 1,
                "showcount": 10,
                "sort": "top",
            },
        )
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
            return []

        return [
            BGGThread(id=thread["threadid"], subject=thread["subject"])
            for thread in response.json().get("threads", [])
        ]

    def get_bgg_thread_content(self, thread_id: str) -> list[BGGComment]:
        response = self.client.get("/api/articles", params={"threadid": thread_id})
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
            return []

        return [
            BGGComment(
                id=item["id"], canonical_link=item["canonical_link"], body=item["body"]
            )
            for item in response.json().get("articles", [])[:6]
        ]
