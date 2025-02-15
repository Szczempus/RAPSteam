# Zadanie: 1_7_4.py
# Input: Jan,Kowalski,1990

from datetime import datetime

imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
rok_urodzenia = int(input("Podaj swój rok urodzenia: "))

aktualny_rok = datetime.now().year
wiek = aktualny_rok - rok_urodzenia

print(f"Nazywasz się {imie} {nazwisko} i masz {wiek} lat.")
