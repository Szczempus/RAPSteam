import os

folder = "dokumenty"

if os.path.exists(folder):
    empty_dirs = [d for d in os.listdir(folder) if
                  os.path.isdir(os.path.join(folder, d)) and not os.listdir(os.path.join(folder, d))]

    for d in empty_dirs:
        os.rmdir(os.path.join(folder, d))
        print(f"Usunięto pusty katalog: {d}")
else:
    print(f"Katalog '{folder}' nie istnieje.")
