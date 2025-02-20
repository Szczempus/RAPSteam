import os

search_folder = "dokumenty"
extension = ".log"

if os.path.exists(search_folder):
    log_files = [f for f in os.listdir(search_folder) if f.endswith(extension)]
    print("\nPliki .log w katalogu 'dokumenty':")
    if log_files:
        for file in log_files:
            print(file)
    else:
        print("Brak plików .log w katalogu.")
else:
    print(f"\nKatalog '{search_folder}' nie istnieje.")
