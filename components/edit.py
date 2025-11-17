import streamlit as st

from agentic.composer import ReviewPost
from commands.blog import generate_post
from database.models import Game


def edit_review():
    if (review := st.session_state.get("review")) and (
        game_query := st.session_state.get("game_query")
    ):
        game: Game = game_query.get("result")

        with st.form("review_editor"):
            _ = st.text_input("Title", value=review.title, key="review_title")
            _ = st.text_area(
                "Body", value=review.body, key="review_body", height="content"
            )
            button = st.form_submit_button("Save")

            if button:
                updated_title = st.session_state.get("review_title") or review.title
                updated_body = st.session_state.get("review_body") or review.body
                generate_post(game, ReviewPost(title=updated_title, body=updated_body))
                st.success("Review saved successfully")
