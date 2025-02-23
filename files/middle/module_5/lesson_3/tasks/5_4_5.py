import pandas as pd
from sklearn.datasets import load_iris

# Wczytanie danych
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]

# Zapis danych do pliku JSON
df.to_json("iris.json", orient="records", indent=4)

# Wczytanie danych z JSON
df_json = pd.read_json("iris.json")

# Obliczenie mediany szerokości działki kielicha dla każdego gatunku
df_median = df_json.groupby("species")["sepal width (cm)"].median()

# Wyświetlenie wyników
print("\nMediana szerokości działki kielicha dla każdego gatunku irysa:")
print(df_median)
