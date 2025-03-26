def recursive_find(lst, target):
    for element in lst:
        if isinstance(element, list):
            if recursive_find(element, target):
                return True
        elif element == target:
            return True
    return False

x = recursive_find("aabcc", "b")
print(x)