class Kot:
    # Atrybut klasowy (wspólny dla wszystkich instancji)
    gatunek = "Felidae"

    def __init__(self, imie, wiek, rasa):
        self.imie = imie  # Atrybut obiektu - imię kota
        self.wiek = wiek  # Atrybut obiektu - wiek kota
        self.rasa = rasa  # Atrybut obiektu - rasa kota

    def mruczenie(self):
        """Metoda zwracająca dźwięk kota"""
        return f"{self.imie} mruczy: Mrrrr... "

    @classmethod
    def zmien_gatunek(cls, nowy_gatunek):
        """Metoda klasy – zmienia atrybut wspólny dla wszystkich kotów"""
        cls.gatunek = nowy_gatunek

    @staticmethod
    def info():
        """Metoda statyczna – nie wymaga dostępu do obiektu"""
        return "Kot to ssak mięsożerny, znany ze swojej niezależności."


# Tworzenie obiektów klasy Kot
kot1 = Kot("Mruczek", 3, "Brytyjski krótkowłosy")
kot2 = Kot("Luna", 2, "Maine Coon")

print(kot1.mruczenie())  # Mruczek mruczy: Mrrrr...
print(kot2.mruczenie())  # Luna mruczy: Mrrrr...
print(Kot.info())  # Kot to ssak mięsożerny, znany ze swojej niezależności.

# Zmiana atrybutu klasowego
Kot.zmien_gatunek("Felis Catus")
print(f"Nowy gatunek kotów: {Kot.gatunek}")  # Nowy gatunek kotów: Felis Catus
