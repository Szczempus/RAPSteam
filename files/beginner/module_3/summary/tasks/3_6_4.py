# Input: 3661

seconds = int(input("Podaj liczbę sekund: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"{hours} godzin, {minutes} minut, {remaining_seconds} sekund")
