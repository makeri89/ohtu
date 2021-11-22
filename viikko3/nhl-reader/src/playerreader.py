import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        
    def fetch_data(self):
        result = []
        response = requests.get(self.url).json()
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['nationality'],
                player_dict['goals'],
                player_dict['assists']
            )
            result.append(player)
        return result
