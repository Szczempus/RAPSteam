# Plik: strings_formatting.py

imie = "Anna"
wiek = 25
waga = 56.51

print(f"{imie} ma {wiek} lat i waży {waga:.2f} kg.")  # "Anna ma 25 lat i waży 56.51 kg."

print("{} ma {} lat i waży {:.2f} kg.".format(imie, wiek, waga))  # "Anna ma 25 lat i waży 56.51 kg."

print("%s ma %d lat i waży %.2f kg." % (imie, wiek, waga))  # "Anna ma 25 lat i waży 56.51 kg."
