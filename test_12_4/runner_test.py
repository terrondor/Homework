import logging
import unittest

from runner import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("Тест", speed=-10)
        except ValueError:
            logging.warning("Неверная скорость для Runner в test_walk.", exc_info=True)
            self.assertTrue(True)
        else:
            logging.warning('Expected ValueError not raised in test_walk.')
            self.fail('Expected ValueError not raised')


    def test_run(self):
        try:
            runner = Runner(123, 5)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner в test_run.", exc_info=True)
            self.assertTrue(True)
        else:
            logging.warning('Expected TypeError not raised in test_run.')
            self.fail('Expected TypeError not raised')


    def test_challenge(self):
        """Test if two runners can maintain different distances"""
        runner_1 = Runner('Test_Runner_1')
        runner_2 = Runner('Test_Runner_2')

        for _ in range(10):
            runner_1.run()
            runner_2.walk()


if __name__=='__main__':
    unittest.main()
