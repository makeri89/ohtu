class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = []
        self.get_players()
        
    def get_players(self):
        self.players = self.reader.fetch_data()
    
    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = [player for player in self.players if player.nationality == nationality]
        players_by_nationality.sort(key=lambda x: x.points, reverse=True)
        return players_by_nationality
