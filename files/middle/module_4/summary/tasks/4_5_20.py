def min_max(lst):
    """Zwraca krotkę zawierającą najmniejszy i największy element listy."""
    return (min(lst), max(lst))


print(min_max([10, 3, 8, 1, 4]))  # Output: (1, 10)
