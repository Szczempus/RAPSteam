import os

filename = "dane2.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"\nPlik '{filename}' został usunięty.")
else:
    print(f"\nPlik '{filename}' nie istnieje, nie można usunąć.")
