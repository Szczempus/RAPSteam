wprowadzenie1 = input("Podaj elementy pierwszego zbioru (oddziel spacjami): ").strip()
zbior1 = set(wprowadzenie1.split())

wprowadzenie2 = input("Podaj elementy drugiego zbioru (oddziel spacjami): ").strip()
zbior2 = set(wprowadzenie2.split())

roznica_zbiorow = zbior1 - zbior2
print("\nRóżnica zbiorów:", roznica_zbiorow)