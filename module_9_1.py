def apply_all_func(int_list, *function):
    results = {}
    for func in function:
        func_name = func.__name__
        results[func_name] = func(int_list)
    return results


def sum_list(lst):
    return lst


def max_list(lst):
    return lst


def min_list(lst):
    return lst


def average_list(lst):
    return sum(lst) / len(lst) if lst else None


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
