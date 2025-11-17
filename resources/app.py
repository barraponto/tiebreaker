import streamlit as st
from app import App
from settings import Settings


@st.cache_resource
def get_app(settings: Settings) -> App:
    return App(settings)
