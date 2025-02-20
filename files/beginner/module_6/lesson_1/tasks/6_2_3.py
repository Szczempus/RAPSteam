from pathlib import Path

current_directory = Path.cwd()
txt_files_recursive = list(current_directory.rglob("*.txt"))

print("\nPliki .txt w bieżącym katalogu i podkatalogach:")
for file in txt_files_recursive:
    print(file)
