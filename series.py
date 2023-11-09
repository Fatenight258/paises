import pandas as pd

datoSerie = pd.Series(["logica","Movile","Base de datos","HTML"],index=["nota1","nota2","nota3","nota4"], dtype="string")
print(datoSerie)

datos = ({"Nombre":"Valentina","Apellido":"Carmona","Sexo":"femenino"})
datosSerie =  pd.Series(datos)
print(datoSerie)