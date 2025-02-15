# Input: 2,3

def obliczPole(szerokosc, wysokosc):
    return szerokosc * wysokosc


print("Podaj szerokość:")
szer = int(input())

print("Podaj wysokość:")
wys = int(input())

pole = obliczPole(szer, wys)
wynik = 2 * (szer + wys)  # Dodana obliczeniowa obwodu

print("Pole:", pole, "Obwód:", wynik)
