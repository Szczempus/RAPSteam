# Input: Jan,Kowalski,18

imie = input("Imię: ")
nazwisko = input("Nazwisko: ")
wiek = input("Wiek: ")

pelne_imie = " ".join([imie, nazwisko])

print(pelne_imie.upper(), pelne_imie.title(), len(nazwisko), type(wiek), sep="\n")
