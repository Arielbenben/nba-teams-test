import requests


players_url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000"


def get_date_from_api(url):
    response = requests.request('GET', url)
    return response.json()


def get_data_of_players_from_api(year: int):
    return get_date_from_api(get_url_per_year(year))

def get_url_per_year(year: int):
    return f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=1000"

# print(get_data_of_players_from_api(2024))