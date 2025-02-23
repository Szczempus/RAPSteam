# Plik: very_advanced_if.py

# Klasyfikacja wyniku
wynik = 85
ocena = "A" if wynik >= 90 else "B" if wynik >= 75 else "C" if wynik >= 60 else "D"

# Sprawdzanie uprawnień użytkownika
uzytkownik, wiek = "moderator", 21
dostep = "Dostęp premium" if uzytkownik in {"admin", "moderator", "vip"} and wiek >= 18 else "Brak uprawnień"

# Skrócony warunek dla temperatury
temp = 25
status_temperatury = "Ciepło" if temp > 20 else "Zimno"

print(ocena, dostep, status_temperatury)
