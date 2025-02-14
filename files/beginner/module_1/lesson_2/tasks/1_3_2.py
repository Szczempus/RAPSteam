# Zadanie: 1_3_2.py

def obliczPole(szerokosc, wysokosc):
    return szerokosc * wysokosc


print("Podaj szerokość:")
szer = int(input())

print("Podaj wysokość:")
wys = int(input())

pole = obliczPole(szer, wys)
obwod = 2 * (szer + wys)  # Dodana obliczeniowa obwodu

print("Pole:", pole, "Obwód:", obwod)
