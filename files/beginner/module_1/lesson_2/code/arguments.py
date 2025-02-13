# Plik: arguments.py

import sys
import time

if len(sys.argv) > 1:
    print(f"Podano argument: {sys.argv[1]}")
else:
    print("Nie podano argumentu.")
time.sleep(10)
