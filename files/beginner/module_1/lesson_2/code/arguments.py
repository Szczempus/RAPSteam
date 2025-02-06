# Plik: arguments.py

import sys

if len(sys.argv) > 1:
    print(f"Podano argument: {sys.argv[1]}")
else:
    print("Nie podano argumentu.")
