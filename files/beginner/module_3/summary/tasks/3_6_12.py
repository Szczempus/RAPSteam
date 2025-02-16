# Input: 44051401359

pesel = input("Podaj numer PESEL: ")
if len(pesel) == 11 and pesel.isdigit():
    print("Data urodzenia:", pesel[:6])
    print("Płeć:", "Kobieta" if int(pesel[-2]) % 2 == 0 else "Mężczyzna")
else:
    print("Błędny PESEL")
