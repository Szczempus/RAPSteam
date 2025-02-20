for i in range(1, 6):
    filename = f"plik{i}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"To jest plik numer {i}")
    print(f"Utworzono: {filename}")
