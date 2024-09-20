import logging
import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger()
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='utf-8',
            format='%(asctime)s | %(levelname)s | %(message)s')


    def test_walk(self):
        try:
            runner = Runner("Тест", speed=-10)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")


    def test_run(self):
        try:
            runner = Runner(123, 5)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


    def test_challenge(self):
        runner_1 = Runner('Test_Runner_1')
        runner_2 = Runner('Test_Runner_2')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__=='__main__':
    unittest.main()
