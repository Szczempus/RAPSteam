class Samochod:
    liczba_samochodow = 0

    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        Samochod.liczba_samochodow += 1

    @classmethod
    def ile_samochodow(cls):
        return f"Liczba utworzonych samochodów: {cls.liczba_samochodow}"


samochod1 = Samochod("Mazda", "6")
samochod2 = Samochod("Opel", "Astra")
samochod3 = Samochod("Renault", "Clio")

print(Samochod.ile_samochodow())
