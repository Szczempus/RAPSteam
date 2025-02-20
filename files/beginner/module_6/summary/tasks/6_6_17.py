import os

folder = "dokumenty"

if os.path.exists(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder)]
    files.sort(key=os.path.getmtime)

    print("\nPliki posortowane według daty modyfikacji:")
    for file in files:
        print(file)
else:
    print(f"Katalog '{folder}' nie istnieje.")
