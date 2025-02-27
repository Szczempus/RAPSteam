class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def przedstaw_sie(self):
        return f"Samochód marki {self.marka}, model {self.model}"


samochod1 = Samochod("Ford", "Focus")
samochod2 = Samochod("BMW", "X5")
samochod3 = Samochod("Audi", "A4")

print(samochod1.przedstaw_sie())
print(samochod2.przedstaw_sie())
print(samochod3.przedstaw_sie())
