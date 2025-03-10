import os
import shutil

current_directory = os.getcwd()
archive_directory = os.path.join(current_directory, 'archiwum')

if not os.path.exists(archive_directory):
    os.makedirs(archive_directory)

for filename in os.listdir(current_directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(current_directory, filename)
        shutil.move(file_path, archive_directory)
