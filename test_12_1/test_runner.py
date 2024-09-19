import unittest
from test_12_1.runner import Runner
from test_12_2.decorator_for_method import skip_if_frozen


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner('Test Runner')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner('Test Runner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner_1 = Runner('Test_Runner_1')
        runner_2 = Runner('Test_Runner_2')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__=='__main__':
    unittest.main()
