# 3_6_9.py
# Input: test@example.com

email = input("Podaj adres e-mail: ")
if "@" in email and "." in email.split("@")[1]:
    print("Poprawny adres e-mail")
else:
    print("Błędny adres e-mail")
