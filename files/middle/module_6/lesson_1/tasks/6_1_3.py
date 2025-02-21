import os

plik = "tkinter.py"
if plik in os.listdir():
    print(f"Uwaga! Plik '{plik}' istnieje w bieżącym katalogu. Może powodować błędy importu!")
else:
    print(f"Plik '{plik}' nie został znaleziony. Tkinter powinien działać poprawnie.")
