# Input: 1234563218

nip = input("Podaj numer NIP: ")

if len(nip) == 10 and nip.isdigit():
    wagi = [6, 5, 7, 2, 3, 4, 5, 6, 7]  # Wagi dla pierwszych 9 cyfr
    suma_kontrolna = sum(int(nip[i]) * wagi[i] for i in range(9))
    if suma_kontrolna % 11 == int(nip[-1]):
        print("Numer NIP jest poprawny.")
    else:
        print("Niepoprawny numer NIP.")
else:
    print("Numer NIP powinien składać się dokładnie z 10 cyfr.")
