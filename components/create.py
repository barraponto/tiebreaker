import streamlit as st
from streamlit_searchbox import st_searchbox

from app import App
from database.models import Game
from database.repository import Repository


def create_review(repo: Repository, app: App):
    def game_search(name: str) -> list[tuple[str, Game]]:
        return [(game.name, game) for game in repo.find_game_by_name(name)[:3]]

    st.markdown("""
    Select a board game to generate a review.
    """)

    game = st_searchbox(
        search_function=game_search, placeholder="Search for a game", key="game_query"
    )
    st.markdown("""
    The system will load the latest reviews threads and look for game highlights to inspire your writing.
    Once generated, you will have the opportunity to edit the review to your liking.
    """)

    if game:
        st.button(f"Generate review for {game.name}", key="add_game")

    if st.session_state.get("add_game"):
        with st.spinner("Generating review..."):
            review = app.generate_review(game)
            st.session_state.update({"review": review})
            st.success("Review generated successfully")
