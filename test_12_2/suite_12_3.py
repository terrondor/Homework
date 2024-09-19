import unittest
from unittest import TextTestRunner
from test_12_1 import test_runner
from test_12_2 import test_runner_2



test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner_2.TournamentTest))

if __name__=='__main__':
    runner = TextTestRunner(verbosity=2)
    runner.run(test_suite)
