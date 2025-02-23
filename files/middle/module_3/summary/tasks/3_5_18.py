
def double_values(d):
    return {k: v * 2 for k, v in d.items()}

print(double_values({'a': 1, 'b': 2, 'c': 3}))  # Wynik: {'a': 2, 'b': 4, 'c': 6}