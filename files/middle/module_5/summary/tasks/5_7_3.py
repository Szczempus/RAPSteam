class Samochod:
    def __init__(self, marka="Nieznana", model="Nieznany"):
        self.marka = marka
        self.model = model


samochod1 = Samochod()
print(samochod1.marka, samochod1.model)
