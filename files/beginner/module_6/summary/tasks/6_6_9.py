import os
import shutil

source_file = "dane.txt"
destination_folder = "Kurs/Python/Projekt"

os.makedirs(destination_folder, exist_ok=True)
destination_path = os.path.join(destination_folder, source_file)

if os.path.exists(source_file):
    shutil.move(source_file, destination_path)
    print(f"Przeniesiono {source_file} do {destination_folder}")
else:
    print(f"Plik {source_file} nie istnieje.")
