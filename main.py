data_structure = [

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])

]


def calculate_structure_sum(*args):
    in_total = 0
    for data in args:
        if isinstance(data, (list, tuple, set)):
            in_total += calculate_structure_sum(*data)
        elif isinstance(data, dict):
            in_total += calculate_structure_sum(*data.keys(), *data.values())
        elif isinstance(data, (int, float)):
            in_total += data
        elif isinstance(data, str):
            in_total += len(data)
    return in_total


result = calculate_structure_sum(data_structure)
print(result)
