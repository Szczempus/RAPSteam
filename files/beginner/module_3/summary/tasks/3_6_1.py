# Input: 15

value = input("Podaj wartość: ")
if value.isdigit() or (value[0] == "-" and value[1:].isdigit()):
    print("Liczba całkowita")
elif value.replace(".", "", 1).isdigit() and value.count(".") == 1:
    print("Liczba zmiennoprzecinkowa")
else:
    print("Tekst")
