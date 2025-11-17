from sqlalchemy import Engine, create_engine


def get_engine(url: str) -> Engine:
    return create_engine(url)
