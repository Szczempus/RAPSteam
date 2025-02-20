import os
import shutil

source_file = "dane.txt"
destination_folder = "dokumenty"
destination_path = os.path.join(destination_folder, source_file)

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

if os.path.exists(source_file):
    shutil.copy(source_file, destination_path)
    print(f"\nPlik '{source_file}' skopiowano do '{destination_folder}'.")
else:
    print(f"\nPlik '{source_file}' nie istnieje, nie można skopiować.")
