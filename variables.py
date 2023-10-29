import pandas as pd

# 1. Importar dataset Comercio.csv creado en Limpieza
comercio = pd.read_csv("data/dataAfterCleaning/Comercio.csv")

# 2. Importar dataset Comercio2021.csv creado en Limpieza
comercio2021 = pd.read_csv("data/dataAfterCleaning/Comercio2021.csv")

# 3. Importar dataset Globo2021.csv creado en Limpieza 
globo2021 = pd.read_csv("data/dataAfterCleaning/Globo2021.csv")

# 4. Importar dataset de códigos sitc - producto
sitc = pd.read_excel("data/dataAfterCleaning/Sitc.xlsx", dtype = str)

# 5. Importar dataset ProductoPaisImp.csv creado en Limpieza
productoPaisImp = pd.read_csv("data/dataAfterCleaning/ProductoPaisImp.csv")

# 6. Importar dataset ProductoPaisExp.csv creado en Limpieza
productoPaisExp = pd.read_csv("data/dataAfterCleaning/ProductoPaisExp.csv")