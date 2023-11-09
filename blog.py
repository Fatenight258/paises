import pandas as pd

continente = pd.read_csv("paises.csv")
#print(continente)

#print(continente.head(5))

continente.to_excel("paises.xlsx",
sheet_name="paises", index=False)
continente2 = pd.read_excel("paises.xlsx",
sheet_name="paises", index=False)
print(continente2)