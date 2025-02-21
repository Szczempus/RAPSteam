#Input: 4

def recursive_sequence(n):
    if n == 0:
        return 1
    else:
        return recursive_sequence(n - 1) + 2

element = int(input("Podaj numer elementu ciągu: "))
print(recursive_sequence(element))
