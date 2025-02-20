import os

directory_name = "dokumenty"
if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    print(f"Katalog '{directory_name}' został utworzony.")
else:
    print(f"Katalog '{directory_name}' już istnieje.")
