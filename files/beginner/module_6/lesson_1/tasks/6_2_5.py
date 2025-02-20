from pathlib import Path

current_directory = Path.cwd()

all_files = [f for f in current_directory.iterdir() if f.is_file()]
py_files = [f for f in all_files if f.suffix == ".py"]

print(f"\nLiczba wszystkich plików w katalogu: {len(all_files)}")
print(f"Liczba plików .py: {len(py_files)}")
