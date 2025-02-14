# Input: 2 3 4 5 6 
wprowadzenie1 = input("Podaj elementy pierwszego zbioru (oddziel spacjami): ").strip()
zbior1 = set(wprowadzenie1.split())

wprowadzenie2 = input("Podaj elementy drugiego zbioru (oddziel spacjami): ").strip()
zbior2 = set(wprowadzenie2.split())

suma_zbiorow = zbior1 | zbior2
print("\nSuma zbiorów:", suma_zbiorow)
