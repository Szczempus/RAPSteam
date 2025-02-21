#Input: 2, 3, 4

def geometric_sequence(a, r, n):
    sequence = []
    for i in range(n):
        sequence.append(a * (r ** i))
    return sequence

a = int(input("Podaj pierwszy element ciągu: "))
r = int(input("Podaj iloraz ciągu: "))
n = int(input("Podaj długość ciągu: "))
print(geometric_sequence(a, r, n))
