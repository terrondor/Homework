import unittest
from pickle import FALSE

from test_12_2.runner_and_tournament import Runner, Tournament
from decorator_for_method import skip_if_frozen


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            results = cls.all_results[key]

            print({pos: runner.name for pos, runner in results.items()})


    def setUp(self):
        self.runner_1 = Runner("Усэйн", speed=10)
        self.runner_2 = Runner("Андрей", speed=9)
        self.runner_3 = Runner("Ник", speed=3)


    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        self.all_results[1] = results
        self.assertTrue(results[1].name=="Усэйн", "Expected winner is Усэйн")


    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        self.all_results[2] = results
        self.assertTrue(results[1].name=="Андрей", "Expected winner is Андрей")


    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        self.all_results[3] = results
        self.assertTrue(results[1].name=="Усэйн", "Expected winner is Усэйн")


if __name__=="__main__":
    unittest.main()
