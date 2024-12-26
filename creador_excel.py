# Instalamos pip install pandas openpyxl
import pandas as pd

# Datagrame es la informacion basica con el nombre de las piezas y centimetro para poder armar el Excel

data = {
    "Piezas": ("Pata", "Tablero", "Puerta", "Estante", "Panel lateral"),
    "Centimetros": [40, 120, 60, 30, 100]
}

df = pd.DataFrame(data)

# Guardar el Dataframe en un archivo Excel
df.to_excel("muebles_medidas.xlsx", index=False)