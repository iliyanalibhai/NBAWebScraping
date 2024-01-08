import requests
from bs4 import BeautifulSoup

url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html' # changed to 2023-2024 season
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing player stats
table = soup.find('table', {'id': 'per_game_stats'})

# Extract player names and points per game for players who scored over 20 points
for row in table.find_all('tr')[1:]:
    player_name = row.find('td', {'data-stat': 'player'})
    points_per_game = row.find('td', {'data-stat': 'pts_per_g'})

    if player_name and points_per_game:
        player_name = player_name.text
        points_per_game = float(points_per_game.text) if points_per_game.text else 0

        if points_per_game > 20:
            print(f"Player: {player_name}, Points Per Game: {points_per_game}")
