import unittest
from test_12_2.runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", speed=10)
        self.runner_2 = Runner("Андрей", speed=9)
        self.runner_3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            results = cls.all_results[key]

            print({pos: runner.name for pos, runner in results.items()})

    def test_race_1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        self.all_results[1] = results
        self.assertTrue(results[1].name == "Усэйн", "Expected winner is Усэйн")

    def test_race_2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        self.all_results[2] = results
        self.assertTrue(results[1].name == "Андрей", "Expected winner is Андрей")

    def test_race_3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        self.all_results[3] = results
        self.assertTrue(results[1].name == "Усэйн", "Expected winner is Усэйн")

if __name__ == "__main__":
    unittest.main()