# Plik: arguments.py
# Inputs: "1" "2" "3"
import sys

if len(sys.argv) > 1:
    print(f"Podano argumenty: {sys.argv[1:]}")
else:
    print("Nie podano argumentów.")
