# Zadanie: 1_6_4.py

lista = [1, 2, 3]
print(f"Pierwotna lista: {lista}")

lista[1] = 5
print(f"Lista po zmianie drugiego elementu: {lista}")

krotka = (4, 5, 6)
print(f"Pierwotna krotka: {krotka}")

try:
    krotka[1] = 7
except TypeError as e:
    print(f"Błąd: {e}")
