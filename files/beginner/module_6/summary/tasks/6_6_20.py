import os

folder = "dokumenty"

if os.path.exists(folder):
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            old_path = os.path.join(folder, file)
            new_path = os.path.join(folder, file.replace(".txt", ".bak"))
            os.rename(old_path, new_path)
            print(f"Zmieniono rozszerzenie: {file} -> {file.replace('.txt', '.bak')}")
else:
    print(f"Katalog '{folder}' nie istnieje.")
