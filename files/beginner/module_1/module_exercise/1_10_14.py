wprowadzenie1 = input("Podaj elementy pierwszego zbioru (oddziel spacjami): ").strip()
zbior1 = set(wprowadzenie1.split())

wprowadzenie2 = input("Podaj elementy drugiego zbioru (oddziel spacjami): ").strip()
zbior2 = set(wprowadzenie2.split())

suma_roz_zbiorow = zbior1 ^ zbior2
print("\nSuma rozłączna (XOR) zbiorów:", suma_roz_zbiorow)