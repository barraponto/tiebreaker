from sqlalchemy import BigInteger, Column, MetaData, Table, Text


games = Table(
    "games",
    MetaData(),
    Column("id", BigInteger),
    Column("yearpublished", BigInteger),
    Column("name", Text),
    Column("is_expansion", BigInteger),
)
