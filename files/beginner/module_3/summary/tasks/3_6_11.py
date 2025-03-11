# Input: 0.89,4.0 

min_obecnosc = 80
min_srednia = 3.5

obecnosc = float(input("Podaj procent obecności: "))
srednia = float(input("Podaj średnią ocen: "))

if obecnosc >= min_obecnosc and srednia >= min_srednia:
    print("Promocja do klasy wyżej")
elif obecnosc < min_obecnosc and srednia < min_srednia:
    print("Musisz powtórzyć rok")
elif obecnosc < min_obecnosc and srednia >= min_srednia: 
    print("Musisz poprawić obecności")
else:
    print("Musisz poprawić oceny")