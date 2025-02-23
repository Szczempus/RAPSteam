
def flatten_list(nested):
    flat_list = []
    for item in nested:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

# Example usage:
nested_list = [1, [2, [3, 4], 5], 6]
print(flatten_list(nested_list))  # Output: [1, 2, 3, 4, 5, 6]
