import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )
        
    def test_search_works(self):
        search_result = self.statistics.search('Kurri')
        self.assertEqual(search_result.name, 'Kurri')
        self.assertEqual(search_result.team, 'EDM')
        
    def test_search_does_not_return_a_player_if_not_found(self):
        search_result = self.statistics.search('Selanne')
        self.assertEqual(search_result, None)
        
    def test_team_search_works(self):
        team_result = self.statistics.team('EDM')
        self.assertEqual(len(team_result), 3)
        self.assertEqual(team_result[0].name, 'Semenko')
        
    def test_top_scorers_limit_works(self):
        top_scorers = self.statistics.top_scorers(3)
        self.assertEqual(len(top_scorers), 3)
        
    def test_top_scorers_works_correctly(self):
        top_scorers = self.statistics.top_scorers(5)
        self.assertEqual(top_scorers[0].name, 'Gretzky')
        self.assertEqual(top_scorers[-1].name, 'Semenko')
