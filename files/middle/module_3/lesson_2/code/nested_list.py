
def print_nested_list(nested):
    for item in nested:
        if isinstance(item, list):
            print_nested_list(item)
        else:
            print(item)

sample_list = [1, [2, 3, [4, 5]], 6]
print_nested_list(sample_list)
