import os

folder = "dokumenty"
if os.path.exists(folder):
    files = os.listdir(folder)
    txt_files = [f for f in files if f.endswith(".txt")]

    print(f"Liczba plików w '{folder}': {len(files)}")
    print(f"Liczba plików .txt: {len(txt_files)}")
else:
    print(f"Katalog '{folder}' nie istnieje.")
