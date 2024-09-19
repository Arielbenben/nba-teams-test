
from toolz import pipe, partial


def calculate_average_season_points(year: int, position: str, data_year):
    sum_all_players = len(data_year)
    sum_all_points = pipe(data_year,
                          partial(filter, lambda x: x.position == position),
                          partial(map, lambda x: x.points),
                          list,
                          sum)
    return sum_all_points / sum_all_players



