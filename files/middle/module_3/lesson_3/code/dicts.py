
# Iteracja po kluczach
person = {"imię": "Anna", "wiek": 28, "miasto": "Warszawa"}
for key in person:
    print(key, "->", person[key])

# Iteracja po parach klucz-wartość
for key, value in person.items():
    print(key, "->", value)
