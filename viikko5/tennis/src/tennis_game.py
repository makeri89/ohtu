class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score = ""
        self.scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1
            
    def handle_even_score(self):
        if self.player1_score <= 3:
            self.score = self.scores[self.player1_score] + "-All"
        else:
            self.score = "Deuce"
            
    def handle_possible_win(self):
        score_difference = self.player1_score - self. player2_score
        if score_difference == 1:
            self.score = "Advantage player1"
        elif score_difference == -1:
            self.score = "Advantage player2"
        elif score_difference >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"
            
    def handle_score_setting(self):
        self.score = self.scores[self.player1_score] \
                     + "-" \
                     + self.scores[self.player2_score]

    def get_score(self):
        if self.player1_score == self.player2_score:
            self.handle_even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            self.handle_possible_win()
        else:
            self.handle_score_setting()

        return self.score
