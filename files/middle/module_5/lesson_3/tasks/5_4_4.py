import pandas as pd
from sklearn.datasets import load_iris

# Wczytanie danych
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]

# Grupowanie według gatunku i obliczenie średniej długości płatka
df_grouped = df.groupby("species")["petal length (cm)"].mean()

# Wyświetlenie wyników
print("\nŚrednia długość płatka dla każdego gatunku irysa:")
print(df_grouped)
