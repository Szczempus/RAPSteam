
def find_min(lst):
    """
    Znajduje najmniejszy element w liście przy użyciu pętli for.
    Parametry:
    lst (list): Lista porównywalnych elementów.
    Zwraca:
    Najmniejszy element w liście.
    """
    if not lst:
        return None

    min_value = lst[0]
    for item in lst:
        if item < min_value:
            min_value = item
    return min_value

numbers = [5, 3, 8, 1, 2, 9, 4]
print(f"Numbers: {numbers}")
print(f"Min value: {find_min(numbers)}")
