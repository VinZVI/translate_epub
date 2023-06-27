values = [
    {"key1": "value1"},
    {"k1": "v1", "k2": "v2", "k3": "v3"},
    {},
    {},
    {"key1": "value1"},
    {"key1": "value1"},
    {"key2": "value2"},
]


def remove_duplicates(array: list(dict())) -> list(dict()):
    for x in array:
        if array.count(x) > 1:
            array.remove(x)
    return array


print(remove_duplicates(values))
