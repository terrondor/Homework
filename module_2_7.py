def print_params(a=1, b='Строка', c=True):
    print(a, b, c)


print_params()
print_params(a=2)
print_params(b=25)
print_params(a=3, b='Urban')
print_params(c=[1, 2, 3])

value_list = [24, 'Win', True]
value_dict = {'Int': 1, 'Str': 'Строка', 'Bool': True}
print_params(*value_list)


def print_params(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print_params(**value_dict)


def print_params(*args):                 # Можно так или нужно было через функцию сделать , немного не понял?
    print(*args)


value_list_2 = [54.32, 'Строка']

print_params(*value_list_2, 42)
