class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def przedstaw_sie(self):
        return f"Samochód marki {self.marka}, model {self.model}"


samochod1 = Samochod("Toyota", "Corolla")
print(samochod1.przedstaw_sie())
