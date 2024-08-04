def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        elif (isinstance(a, (int, float)) and isinstance(b, str)) or (
                isinstance(a, str) and isinstance(b, (int, float))):
            return str(a) + str(b)
        else:

            return a + b
    except:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))  # Вывод: '123.456строка'
print(add_everything_up('яблоко', 4215))  # Вывод: 'яблоко4215'
print(add_everything_up(123.456, 7))  # Вывод: 130.456
print(add_everything_up([1, 2], (3, 4)))  # Вывод: '[1, 2](3, 4)'
