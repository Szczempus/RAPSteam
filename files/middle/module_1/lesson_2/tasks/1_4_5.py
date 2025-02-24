# Zadanie: 1_7_5.py
# Input: 3,5,1

liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))
liczba3 = int(input("Podaj trzecią liczbę całkowitą: "))

srednia = (liczba1 + liczba2 + liczba3) / 3

maksymalna = max(liczba1, liczba2, liczba3)
minimalna = min(liczba1, liczba2, liczba3)
roznica = maksymalna - minimalna

print(f"Średnia z podanych liczb to: {srednia:.2f}. Różnica między największą a najmniejszą liczbą to: {roznica}.")
