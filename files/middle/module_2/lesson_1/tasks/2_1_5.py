# Input: Matematyka,3,Informatyka,5,Chemia,4

oceny = {
    input("Podaj przedmiot 1: "): int(input("Podaj ocenę: ")),
    input("Podaj przedmiot 2: "): int(input("Podaj ocenę: ")),
    input("Podaj przedmiot 3: "): int(input("Podaj ocenę: "))
}

for przedmiot, ocena in oceny.items():
    print(f"{przedmiot}: {ocena}")
