import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
if os.path.exists(desktop_path):
    print("\nZawartość katalogu Pulpit:")
    for item in os.listdir(desktop_path):
        print(item)
else:
    print("\nKatalog 'Pulpit' nie istnieje.")
