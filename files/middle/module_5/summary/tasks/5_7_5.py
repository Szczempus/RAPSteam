class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def przedstaw_sie(self):
        return f"Samochód marki {self.marka}, model {self.model}"


class ElektrycznySamochod(Samochod):
    def __init__(self, marka, model, pojemnosc_baterii=50):
        super().__init__(marka, model)
        self.pojemnosc_baterii = pojemnosc_baterii

    def przedstaw_sie(self):
        return f"Samochód marki {self.marka}, model {self.model}, bateria: {self.pojemnosc_baterii} kWh"


samochod3 = ElektrycznySamochod("Tesla", "Model 3")
print(samochod3.przedstaw_sie())
