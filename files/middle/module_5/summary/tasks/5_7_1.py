class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model


samochod1 = Samochod("Toyota", "Corolla")
print(samochod1.marka, samochod1.model)
