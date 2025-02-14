# Input: 4 5 3 2
wprowadzenie = input("Podaj oceny oddzielone spacjami (np. 4 5 3 2): ").strip()
oceny = []

for ocena in wprowadzenie.split():
    oceny.append(int(ocena))

srednia = sum(oceny) / len(oceny)
print(f"\nŚrednia ocen: {srednia:.2f}")
