# Input: Jan Kowalski

imie = input("Imię: ")
nazwisko = input("Nazwisko: ")

print("Za pomocą +:", imie + " " + nazwisko)
print("Za pomocą join():", " ".join([imie, nazwisko]))
print("Wielkimi literami:", (imie + " " + nazwisko).upper())
