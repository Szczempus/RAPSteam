def oblicz_cene(ilosc, cena_za_sztuke, rabat=0):
    if (ilosc > 10):
        rabat = 0.1
    elif ilosc > 5:
        rabat = 0.05
    else:
        rabat = 0
    cena_koncowa = (ilosc * cena_za_sztuke) * (1 - rabat)
    return cena_koncowa


print(oblicz_cene(7, 20))
print(oblicz_cene(12, 15))
