class Player:
    def __init__(self, name, team, nationality,
                 goals, assists):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
        self.points = goals + assists
    
    def __str__(self):
        return f'{self.name:20}{self.team} {str(self.goals):>2} + {str(self.assists):>2} = {str(self.points):<3}'
