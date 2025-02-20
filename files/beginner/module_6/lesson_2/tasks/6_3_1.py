filename = "dane.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        print("\nZawartość pliku:")
        for line in file:
            print(line.strip())  # Usuwa zbędne białe znaki na końcu
except FileNotFoundError:
    print(f"\nPlik '{filename}' nie istnieje.")
