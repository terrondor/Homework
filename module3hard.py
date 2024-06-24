data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    total_sum = 0

    for element in data:
        if isinstance(element, int):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, list):
            total_sum += calculate_structure_sum(element)
        elif isinstance(element, dict):
            total_sum += calculate_structure_sum(list(element.values()))
        elif isinstance(element, tuple):
            for item in element:
                total_sum += calculate_structure_sum([item])
        elif isinstance(element, list) and isinstance(element[0], tuple):

            total_sum += calculate_structure_sum(element[0])

    return total_sum


result = calculate_structure_sum(data_structure)
print(result)
