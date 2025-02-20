from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")  # DD-MM-YYYY HH:MM:SS
print("Aktualna data i czas:", formatted_date)
