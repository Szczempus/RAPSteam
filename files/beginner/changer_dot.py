import os

module_path = "module_3"  # Ścieżka do głównego folderu

for root, dirs, files in os.walk(module_path):
    if os.path.basename(root) == "tasks":  # Sprawdzamy, czy jesteśmy w folderze 'tasks'
        for file in files:
            print(file)  # Wyświetlenie oryginalnej nazwy pliku
            if file.endswith(".py") and file.count(".") == 3:  # Sprawdzamy format 'x.x.x.py'
                old_path = os.path.join(root, file)
                base_name, ext = file.rsplit(".", 1)  # Oddzielenie rozszerzenia .py
                new_base_name = base_name.replace(".", "_", 2)  # Zamiana dwóch pierwszych kropek na "_"
                new_file = f"{new_base_name}.{ext}"  # Połączenie nowej nazwy z .py
                new_path = os.path.join(root, new_file)

                os.rename(old_path, new_path)  # Zmiana nazwy pliku
                print(f"Zmieniono: {old_path} -> {new_path}")
