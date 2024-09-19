import unittest


def skip_if_frozen(func):
    def wrapper(*args, **kwargs):
        if args[0].is_frozen:
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return func(*args, **kwargs)

    return wrapper



