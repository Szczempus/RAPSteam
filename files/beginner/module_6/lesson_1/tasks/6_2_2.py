from pathlib import Path

current_directory = Path.cwd()
txt_files = list(current_directory.glob("*.txt"))

print("\nPliki .txt w bieżącym katalogu:")
for file in txt_files:
    print(file.name)
