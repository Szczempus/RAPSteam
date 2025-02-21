def calculate_average(lst):
    total = 0
    for num in lst:
        total += num
    average = total / len(lst) if lst else 0
    return average

lst = [1, 2, 3, 4, 5]  
print(f"Średnia listy: {lst} wynosi: {calculate_average(lst)}")

