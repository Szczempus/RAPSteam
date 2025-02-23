# Tworzenie słownika
osoba = {
    "imie": "Anna",
    "wiek": 30,
    "miasto": "Warszawa"
}

# Dodawanie nowych kluczy
osoba["email"] = "anna@example.com"

# Usuwanie elementu
del osoba["wiek"]

# Iteracja po słowniku
for klucz, wartosc in osoba.items():
    print(f"{klucz}: {wartosc}")

# Dostęp do wartości
print(osoba["imie"])  # "Anna"
