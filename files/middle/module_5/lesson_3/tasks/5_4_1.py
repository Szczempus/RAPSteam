import pandas as pd
from sklearn.datasets import load_iris

# Wczytanie danych z biblioteki sklearn
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Dodanie kolumny z nazwą gatunku
df["species"] = [iris.target_names[i] for i in iris.target]

# Podgląd pierwszych 5 wierszy
print("Podgląd danych:")
print(df.head())

# Informacje o zbiorze danych
print("\nInformacje o zbiorze danych:")
print(df.info())
