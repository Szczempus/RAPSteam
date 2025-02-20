import os
from datetime import datetime, timedelta

current_directory = os.getcwd()
files_in_directory = os.listdir(current_directory)
time_threshold = datetime.now() - timedelta(days=1)

print("\nPliki utworzone lub zmodyfikowane w ciągu ostatnich 24 godzin:")
for file in files_in_directory:
    file_path = os.path.join(current_directory, file)
    if os.path.isfile(file_path):
        modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        if modification_time > time_threshold:
            print(f"{file} - {modification_time.strftime('%Y-%m-%d %H:%M:%S')}")
