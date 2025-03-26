
def while_sum(lst):
    total = 0
    index = 0
    while index < len(lst):
        total += lst[index]
        index += 1
    return total

print(while_sum([1,2,3,4]))