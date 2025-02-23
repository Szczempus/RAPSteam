import pandas as pd
from sklearn.datasets import load_iris

# Wczytanie danych
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]

# Sortowanie według długości płatka (malejąco)
df_sorted = df.sort_values(by="petal length (cm)", ascending=False)

# Wyświetlenie pierwszych 5 wierszy posortowanych danych
print("\nDane posortowane według długości płatka (malejąco):")
print(df_sorted.head())
