filename = "notatka.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write("To jest pierwsza linia.\n")
    file.write("To jest druga linia.\n")
    file.write("To jest trzecia linia.\n")

print(f"\nPlik '{filename}' został nadpisany.")
