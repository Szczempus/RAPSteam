# Input: Jan,Kowalski

imie = input("Podaj imię: ").strip()
nazwisko = input("Podaj nazwisko: ").strip()

imie_wielkie = imie.upper()
nazwisko_cap = nazwisko.capitalize()

print(f"\nWitaj {imie_wielkie} {nazwisko_cap}!")
