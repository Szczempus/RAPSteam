import os
from datetime import datetime

search_folder = "dokumenty"

if os.path.exists(search_folder):
    print("\nInformacje o plikach w katalogu 'dokumenty':")
    for file in os.listdir(search_folder):
        file_path = os.path.join(search_folder, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path) / 1024  # w KB
            modification_time = os.path.getmtime(file_path)
            formatted_time = datetime.fromtimestamp(modification_time).strftime("%Y-%m-%d %H:%M:%S")
            print(f"{file} - {file_size:.2f} KB - Ostatnia modyfikacja: {formatted_time}")
else:
    print(f"\nKatalog '{search_folder}' nie istnieje.")
