import pandas as pd

df = pd.DataFrame({"Dzień": ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Ndz"], "Numer": range(1, 8)})
df.to_csv("dni_tygodnia.csv", index=False)
print(df)
