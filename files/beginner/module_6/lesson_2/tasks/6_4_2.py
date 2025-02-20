# Input: YYYY-MM-DD

from datetime import datetime

date1_str = input("\nPodaj pierwszą datę (YYYY-MM-DD): ")  # Input: np. 2025-02-20
date2_str = input("Podaj drugą datę (YYYY-MM-DD): ")  # Input: np. 2025-03-05

try:
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    difference = abs((date2 - date1).days)
    print(f"Różnica dni między {date1_str} a {date2_str}: {difference} dni")
except ValueError:
    print("Błąd: Niepoprawny format daty. Wprowadź w formacie YYYY-MM-DD.")
