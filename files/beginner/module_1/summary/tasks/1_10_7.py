from datetime import datetime

now = datetime.now()

format1 = now.strftime("%m-%d-%Y %H:%M:%S")
format2 = now.strftime("%d/%m/%Y %H:%M:%S")

print("Format 1:", format1)
print("Format 2:", format2)