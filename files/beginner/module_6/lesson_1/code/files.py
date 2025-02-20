import os

# Tworzenie nowego pliku
file_path = "rap_steak.txt"

# Tryb 'w' tworzy plik lub nadpisuje, 'x' tworzy tylko, jeśli nie istnieje
with open(file_path, 'w') as file:
    file.write("To jest przykładowa zawartość pliku.\n")

print(f"Plik '{file_path}' został utworzony.")

# Tworzenie katalogu
dir_name = "folder"

try:
    os.mkdir(dir_name)
    print(f"Katalog '{dir_name}' został utworzony.")
except FileExistsError:
    print(f"Katalog '{dir_name}' już istnieje.")

# Tworzenie zagnieżdżonej struktury katalogów
nested_dir = "folder/podfolder"

os.makedirs(nested_dir, exist_ok=True)
print(f"Katalog '{nested_dir}' został utworzony.")
