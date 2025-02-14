# Argumenty: 1 2 3

import sys

# Pobranie argumentów (pomijając nazwę skryptu)
arguments = sys.argv[1:]

# Sprawdzenie, czy podano argumenty
if arguments:
    print(f"Podano {len(arguments)} argumentów: {', '.join(arguments)}")
else:
    print("Nie podano argumentów!")
