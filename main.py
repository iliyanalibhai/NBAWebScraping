import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html' # changed to 2023-2024 season
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# find the table containing player stats
table = soup.find('table', {'id': 'per_game_stats'})

# scrapping for players who average at least 20 points per game

players_avging_20 = []
point_vals = []
print("PLAYERS AVERAGING 20 OR MORE:")
for row in table.find_all('tr')[1:]: # skip header
    player_name = row.find('td', {'data-stat': 'player'}) # scraps the <td> element with the attribute 'data-stat': 'player'
    points_per_game = row.find('td', {'data-stat': 'pts_per_g'}) # scraps the <td> element with the attribute 'data-stat': 'player'

    if player_name and points_per_game: # if not null or nontype
        player_name = player_name.text
        points_per_game = float(points_per_game.text) if points_per_game.text else 0

        if points_per_game > 20:
            print(f"Player: {player_name}, Points Per Game: {points_per_game}")
            players_avging_20.append(player_name) 
            point_vals.append(points_per_game)



# scrap for players who are currently averaging 25 or more
print("PLAYERS AVERAGING 25 OR MORE:")
for row in table.find_all('tr')[1:]:
    player_name = row.find('td', {'data-stat': 'player'}) # extract player name
    points_per_game = row.find('td', {'data-stat': 'pts_per_g'}) # extract ppg

    if player_name and points_per_game:
        player_name = player_name.text # set variable to be playername
        points_per_game = float(points_per_game.text) if points_per_game.text else 0

        if points_per_game >= 25: # if greater than or equal then putput name and ppg
            print(f"Player: {player_name}, Points Per Game: {points_per_game}")

# Players averaging a double double, at least 10 points and assist, points and rebounds, assist and rebounds (rare)


for row in table.find_all('tr')[1:]:
    player_name = row.find('td', {'data-stat': 'player'}) # extract player name
    points_per_game = row.find('td', {'data-stat': 'pts_per_g'}) # extract ppg
    rebounds_per_game = row.find('td', {'data-stat': 'trb_per_g'}) #extract rebound per game
    assists_per_game = row.find('td', {'data-stat': 'ast_per_g'}) # extract assist per game

    if player_name and points_per_game and rebounds_per_game and assists_per_game: # if none of these are null 
        player_name = player_name.text
        points = float(points_per_game.text) if points_per_game.text else 0
        rebounds = float(rebounds_per_game.text) if rebounds_per_game.text else 0
        assists = float(assists_per_game.text) if assists_per_game.text else 0

        if points >= 10 and rebounds >= 10:
            print(f"Player: {player_name}, Points Per Game: {points}, Rebounds Per Game: {rebounds}")
        if points >= 10 and assists >= 10:
            print(f"Player: {player_name}, Points Per Game: {points}, Assist Per Game: {assists}")


plt.figure(figsize=(12, 6))
bar_width = 0.4  # adjust the width of the bars
plt.bar(players_avging_20, point_vals, color='skyblue',width=bar_width)
plt.xlabel('Players') # x axis label
plt.ylabel('Points per Game') # y axis label
plt.title('Players Averaging 20+ Points per Game') # graph title
plt.xticks(rotation=90) # looked this up, basically means rotates the labels, more room?
plt.ylim(0, max(point_vals) + 5,)  # adjust the y-axis limit
plt.yticks(range(0, int(max(point_vals)) + 5, 2))  # Set y-axis intervals
plt.tight_layout()

plt.show()