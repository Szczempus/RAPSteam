import os

old_filename = "dane.txt"
new_filename = "archiwum.txt"

if os.path.exists(old_filename):
    os.rename(old_filename, new_filename)
    print(f"\nPlik '{old_filename}' został zmieniony na '{new_filename}'.")
else:
    print(f"\nPlik '{old_filename}' nie istnieje, nie można zmienić nazwy.")
