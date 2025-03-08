import os
from pathlib import Path

# Przeglądanie zawartości katalogu za pomocą os
folder = "C:\\"
print("Pliki i katalogi w bieżącym katalogu:", os.listdir(folder))

# Wyszukiwanie plików .txt za pomocą pathlib
txt_files = list(Path(folder).glob("*.txt"))
print("Pliki tekstowe w katalogu:", [file.name for file in txt_files])
