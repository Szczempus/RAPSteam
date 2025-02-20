filename = "log.txt"
output_filename = "log_cleaned.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(output_filename, "w", encoding="utf-8") as file:
        for line in lines:
            if "ERROR" not in line:
                file.write(line)

    print(f"\nUtworzono nowy plik '{output_filename}' bez linii zawierających 'ERROR'.")
except FileNotFoundError:
    print(f"\nPlik '{filename}' nie istnieje.")
