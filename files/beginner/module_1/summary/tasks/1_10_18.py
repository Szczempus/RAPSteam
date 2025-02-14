imie = input("Podaj imię: ").strip()
nazwisko = input("Podaj nazwisko: ").strip()
wiek = int(input("Podaj wiek: ").strip())
zawod = input("Podaj zawód: ").strip()

dane_uzytkownika = {
    "imię": imie,
    "nazwisko": nazwisko,
    "wiek": wiek,
    "zawód": zawod
}

print("\nDane użytkownika:", dane_uzytkownika)