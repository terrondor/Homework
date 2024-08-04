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
            raise TypeError("Unsupported types")
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))