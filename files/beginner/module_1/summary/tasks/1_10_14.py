# Input: 1 2 3 5, 4 5 6 7

wprowadzenie1 = input("Podaj elementy pierwszego zbioru (oddziel spacjami): ").strip()
zbior1 = set(wprowadzenie1.split())

wprowadzenie2 = input("Podaj elementy drugiego zbioru (oddziel spacjami): ").strip()
zbior2 = set(wprowadzenie2.split())

czesc_wspolna = zbior1 & zbior2
print("Część wspólna zbiorów:", czesc_wspolna)
