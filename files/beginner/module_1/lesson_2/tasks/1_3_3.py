# Argumenty: 1

import sys

# Sprawdzenie, czy podano argument
if len(sys.argv) > 1:
    argument = sys.argv[1]
    print(f"Podany argument: {argument}")
else:
    print("Nie podano argumentu!")
