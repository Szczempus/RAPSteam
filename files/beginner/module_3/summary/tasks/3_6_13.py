# Input: 12.05.2023

data = input("Podaj datę (YYYY-MM-DD, DD.MM.YYYY, MM/DD/YYYY): ")

if "-" in data:  # Format YYYY-MM-DD
    rok, miesiac, dzien = data.split("-")
elif "." in data:  # Format DD.MM.YYYY
    dzien, miesiac, rok = data.split(".")
elif "/" in data:  # Format MM/DD/YYYY
    miesiac, dzien, rok = data.split("/")
else:
    print("Nieznany format daty.")
    exit()

# Konwersja do standardowego formatu YYYY-MM-DD
sformatowana_data = f"{rok}-{miesiac.zfill(2)}-{dzien.zfill(2)}"
print("Data w formacie YYYY-MM-DD:", sformatowana_data)
