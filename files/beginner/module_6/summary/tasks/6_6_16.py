import os

path = input("Podaj ścieżkę: ")

if os.path.exists(path):
    if os.path.isfile(path):
        print(f"{path} jest plikiem.")
    elif os.path.isdir(path):
        print(f"{path} jest katalogiem.")
else:
    print("Podana ścieżka nie istnieje.")
