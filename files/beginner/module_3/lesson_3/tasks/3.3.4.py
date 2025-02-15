# Input: 1 2 3 4

lista = input("Podaj liczby [1 2 3 4]:").split()
if any(int(num) % 2 == 0 for num in lista) and all(int(num) >= 0 for num in lista):
    print("Lista spełnia warunki")
else:
    print("Lista nie spełnia warunków")
