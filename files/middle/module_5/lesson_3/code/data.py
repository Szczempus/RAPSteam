import pandas as pd
from sklearn.datasets import load_iris

# 1. Wczytanie gotowych danych z biblioteki sklearn
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Dodanie kolumny z nazwami gatunków
df["species"] = [iris.target_names[i] for i in iris.target]

# 2. Podgląd danych
print("Podgląd danych:", df.head(2))

# 3. Filtrowanie danych - wybór kwiatów o długości płatka większej niż 5 cm
df_powyzej_5 = df[df["petal length (cm)"] > 5]
print("\nKwiaty o długości płatka większej niż 5 cm:", df_powyzej_5.head(2))

# 4. Sortowanie według szerokości działki kielicha (malejąco)
df_sorted = df.sort_values(by="sepal width (cm)", ascending=False)
print("\nSortowanie według szerokości działki kielicha (malejąco):", df.head(2))

# 5. Średnia długość płatka dla każdego gatunku
df_srednia_dlugosc = df.groupby("species")["petal length (cm)"].mean()
print("\nŚrednia długość płatka dla każdego gatunku:", df.head(2))

# 6. Dodanie nowej kolumny "stosunek_płatka" (stosunek długości do szerokości płatka)
df["stosunek_płatka"] = df["petal length (cm)"] / df["petal width (cm)"]
print("\nDodanie kolumny 'stosunek_płatka':", df.head(2))

# 7. Zmiana nazw gatunków na wielkie litery
df["species"] = df["species"].str.upper()
print("\nZmiana nazw gatunków na wielkie litery:", df.head(2))

# 8. Usunięcie wierszy, gdzie szerokość działki kielicha jest mniejsza niż 3 cm
df = df[df["sepal width (cm)"] >= 3]
print("\nUsunięcie kwiatów o szerokości działki kielicha mniejszej niż 3 cm:", df.head(2))
