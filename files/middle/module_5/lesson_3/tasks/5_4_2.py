import pandas as pd
from sklearn.datasets import load_iris

# Wczytanie danych
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]

# Filtrowanie danych według warunków
df_filtered = df[(df["petal length (cm)"] > 5) & (df["sepal width (cm)"] >= 3)]

# Wyświetlenie przefiltrowanych danych
print("\nKwiaty o długości płatka większej niż 5 cm i szerokości działki kielicha co najmniej 3 cm:")
print(df_filtered)
