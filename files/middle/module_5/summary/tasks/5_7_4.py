class Samochod:
    def __init__(self, marka="Nieznana", model="Nieznany"):
        self.marka = marka
        self.model = model


samochod1 = Samochod()
print(samochod1.marka, samochod1.model)


class ElektrycznySamochod(Samochod):
    def __init__(self, marka, model, pojemnosc_baterii=50):
        super().__init__(marka, model)
        self.pojemnosc_baterii = pojemnosc_baterii


samochod2 = ElektrycznySamochod("Tesla", "Model S")
print(samochod2.marka, samochod2.model, samochod2.pojemnosc_baterii, "kWh")
