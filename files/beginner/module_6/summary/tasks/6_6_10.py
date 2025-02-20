source_file = "dane.txt"
destination_file = "kopia_dane.txt"

try:
    with open(source_file, "r", encoding="utf-8") as infile, open(destination_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            outfile.write(line)
    print(f"Zawartość skopiowano do {destination_file}")
except FileNotFoundError:
    print(f"Plik {source_file} nie istnieje.")
