import os

filename = "dane.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"\nPlik '{filename}' został usunięty.")
else:
    print(f"\nPlik '{filename}' nie istnieje, nie można usunąć.")
