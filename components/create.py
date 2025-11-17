import streamlit as st
from streamlit_searchbox import st_searchbox

from database.repository import Repository


def create_review(repo: Repository):
    query = st.session_state.get("game_query")

    def game_search(name: str) -> list[str]:
        return [game.name for game in repo.find_game_by_name(name)[:3]]

    st_searchbox(
        search_function=game_search, placeholder="Search for a game", key="game_query"
    )

    if query and (result := query.get("result")):
        _ = st.button(f"Generate review for {result}", key="add_game")
