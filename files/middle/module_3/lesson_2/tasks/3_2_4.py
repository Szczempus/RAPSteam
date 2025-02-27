
def suma_cyfr(liczba):
    if liczba == 0:
        return 0
    else:
        reszta = liczba % 10
        suma = reszta + suma_cyfr(liczba // 10)
        return suma

print(suma_cyfr(1234)) 