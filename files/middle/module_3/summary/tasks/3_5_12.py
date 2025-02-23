
def while_sum(lst):
    total = 0
    index = 0
    while index < len(lst):
        total += lst[index]
        index += 1
    return total
