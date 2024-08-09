def add_everything_up(a, b):
    try:
        return a + b
    except Exception:
        return str(a) + str(b)


# Тестирование функции с предоставленными примерами
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
