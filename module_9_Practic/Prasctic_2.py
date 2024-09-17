# Задача - есть функция, которая возвращает результат введения числа a  степень b
# Нужно ускорить ее, чтобы она не делала повторные вычисления


def memoize_func(f):
    mem = {}

    def wrapper(*args):
        print(f'Выполнение функции с аргментами = {args}, внутренняя память = {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась, ответ = {mem[args]}'
        else:
            return f'Функция уже была выполнена раньше, ответ = {mem[args]}'

    return wrapper


@memoize_func
def func(a, b):
    print(f'   Вычисляем функцию с аргументами ({a}, {b})')
    return a ** b


print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')
