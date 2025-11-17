# work on data dump from bgg: https://boardgamegeek.com/data_dumps/bg_ranks
generate-database:
    qsv select id,yearpublished,name,is_expansion data/boardgames_ranks.csv > data/games.csv
    qsv to sqlite data/games.sqlite data/games.csv
    rm data/games.csv

[working-directory: './blog']
generate-post gameid title:
    uv run nikola new_post -t "{{title}}" --format markdown --import template.markdown posts/{{gameid}}.md

[working-directory: './blog']
generate-site:
    uv run nikola build
