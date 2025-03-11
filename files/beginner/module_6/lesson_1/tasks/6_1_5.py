import os
import shutil

current_directory = "C:\\Kurs"
archive_directory = os.path.join(current_directory, 'archiwum')

if not os.path.exists(archive_directory):
    print(f"Tworzę folder: {archive_directory}")
    os.makedirs(archive_directory)
else:
    print(f"Folder już istnieje: {archive_directory}")

for filename in os.listdir(current_directory):
    if filename.endswith('.txt'):
        print(f"Przenoszę plik: {filename}")
        file_path = os.path.join(current_directory, filename)
        shutil.move(file_path, archive_directory)
        
print("Zakończono przenoszenie plików.")