import os

nested_directories = "dokumenty/projekty/python"
if not os.path.exists(nested_directories):
    os.makedirs(nested_directories)
    print(f"Struktura katalogów '{nested_directories}' została utworzona.")
else:
    print(f"Struktura katalogów '{nested_directories}' już istnieje.")
