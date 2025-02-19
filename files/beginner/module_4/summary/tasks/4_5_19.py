# Input: Jan 30

name, age = input("Podaj imię i wiek: ").split()
person = {"Imię": name, "Wiek": int(age)}
person["Wiek"] += 1
print(f"Zaktualizowany słownik: {person}")
