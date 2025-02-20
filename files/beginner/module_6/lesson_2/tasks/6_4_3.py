from datetime import timedelta, datetime

now = datetime.now()
future_date = now + timedelta(days=7)
print("\nData po dodaniu 7 dni:", future_date.strftime("%d-%m-%Y %H:%M:%S"))
