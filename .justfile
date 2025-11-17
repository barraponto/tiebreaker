# work on data dump from bgg: https://boardgamegeek.com/data_dumps/bg_ranks
generate-database:
    qsv select id,yearpublished,name data/boardgames_ranks.csv > data/games.csv
    qsv to sqlite data/games.sqlite data/games.csv
    rm data/games.csv
