import tempfile

with tempfile.NamedTemporaryFile(mode="w+", delete=True, encoding="utf-8") as temp_file:
    temp_file.write("To jest plik tymczasowy\n")
    temp_file.seek(0)
    print(temp_file.read())  # Wyświetla zawartość
print("Plik tymczasowy został usunięty automatycznie.")
