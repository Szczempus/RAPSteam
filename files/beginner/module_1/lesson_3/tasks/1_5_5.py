imie, nazwisko = "Jan", "Kowalski"
pelne_plus = imie + nazwisko
pelne_join = " ".join([imie.lower(), nazwisko.lower()])
pelne_upper = pelne_plus.upper()

print(pelne_plus, type(pelne_plus), len(pelne_plus))
print(pelne_join)
print(pelne_upper)
