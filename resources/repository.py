import streamlit as st
from database.repository import Repository
from settings import Settings


@st.cache_resource
def get_repository(settings: Settings) -> Repository:
    return Repository(settings)
