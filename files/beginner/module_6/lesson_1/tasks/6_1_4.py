filename = "log.txt"

# Tworzenie i zapis do pliku
with open(filename, "w", encoding="utf-8") as file:
    file.write("Linia 1: Przykładowy tekst.\n")
    file.write("Linia 2: Kolejna linia w pliku.\n")
    file.write("Linia 3: Ostatnia linia logu.\n")

print(f"Plik '{filename}' został utworzony i zapisany.")

# Odczyt i wyświetlenie zawartości pliku
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

print("\nZawartość pliku:")
print(content)
