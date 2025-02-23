# Plik: strings.py
# Input: Witaj w Pythonie!

tekst = input("Podaj tekst: ")

print(len(tekst))  # 17, długość tekstu
print(tekst.upper())  # "WITAJ W PYTHONIE!" - zamiana na wielkie litery
print(tekst.lower())  # "witaj w pythonie!" - zamiana na małe litery
print(tekst.replace("Pythonie", "świecie"))  # "Witaj w świecie!" - zamiana fragmentu tekstu
print(tekst.strip())  # "Witaj w Pythonie!" - usunięcie białych znaków na początku i końcu
