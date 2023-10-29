# 1. Importamos librería Pandas
import pandas as pd

# 2. Importamos la relación código SITC - nombre producto en la variable metadataSITC
# 3. Cambiamos el nombre de la columna Key a SITC
# 4. Eliminamos la columna Description
def LimpiezaDatasetInicial(metadataSITC, metadataCountries, data):
    metadataSITC = metadataSITC.rename(columns={"Key": "SITC"})
    metadataSITC = metadataSITC.drop(labels = "Description", axis = 1)

# 5. Importamos los datos de comercio exterior de Países Bajos en variables data20xx
# 6. Eliminamos la columna ID, BalanceOfTrade_3, ChangeInImportValue_4 y ChangeInExportValue_5

    data = data.drop(labels = "ID", axis = 1)
    data = data.drop(labels = "BalanceOfTrade_3", axis = 1)
    data = data.drop(labels = "ChangeInImportValue_4", axis = 1)
    data = data.drop(labels = "ChangeInExportValue_5", axis = 1)

# 7. Hacemos un merge de metadataSITC y data (columna SITC en común). Llamamos datasetmerge1 al nuevo set de datos

    datasetmerge = pd.merge(metadataSITC, data)

# 8. Importamos la relación código país - nombre país en la variable metadataCountries
# 9. Cambiamos el nombre de la columna Key a Countries
# 10. Eliminamos la columna Description

    metadataCountries = metadataCountries.rename(columns={"Key": "Countries"})
    metadataCountries = metadataCountries.drop(labels = "Description", axis = 1)

# 11. Hacemos un merge de datasetmerge1 y metadataCountries (columna Countries en común). LLamamos dataset al nuevo set de datos

    dataset = pd.merge(datasetmerge, metadataCountries, on = "Countries")

# 12. Eliminamos la columna Countries de dataset
# 13. Renombramos columnas del dataset (nuevas columnas en español y reflejando unidades)

    dataset = dataset.drop(labels = "Countries", axis = 1)
    dataset = dataset.rename(columns={"Title_x": "Productos", "Title_y": "Países", "Periods": "Año", "ImportValue_1": "Importaciones (millones de €)", "ExportValue_2": "Exportaciones (millones de €)"})
    return dataset

# 14. Eliminamos la columna SITC de dataset
def LimpiezaDatasetPosterior(dataset):
    dataset = dataset.drop(labels = "SITC", axis = 1)

# 15. Separamos de la columna Productos de dataset el código SITC y el nombre de producto. Los introducimos en las variables codigo y producto.

    productoSeparado = dataset["Productos"].str.split(expand=True, n=1)
    codigo = productoSeparado[[0]]
    codigo.columns = ['SITC Nivel 3'] 

# 16. Corregimos el primer nombre de producto

    producto = productoSeparado[[1]]
    producto.columns = ['Producto']
    producto = producto.copy()
    producto["Producto"][0] = "Total goods"

# 17. Hacemos un merge de dataset, codigo y producto (índice en común). LLamamos comercio al nuevo set de datos

    comercioPrevio = pd.merge(dataset, codigo, left_index=True, right_index=True)
    comercio = pd.merge(comercioPrevio, producto, left_index=True, right_index=True)

# 18. Eliminamos la columna Productos

    comercio = comercio.drop(["Productos"], axis = 1)

# 19. Eliminamos todas aquellas filas con NaN en las cinco columnas de comercio exterior

    comercio = comercio.dropna(axis='rows', thresh=5)

# 20. Ordenamos las columnas

    first_column = comercio.pop('Países')
    comercio.insert(0, 'Países', first_column)
    first_column = comercio.pop('Producto')
    comercio.insert(0, 'Producto', first_column)
    first_column = comercio.pop('SITC Nivel 3')
    comercio.insert(0, 'SITC Nivel 3', first_column)

# 21. Nos quedamos solo con las filas cuyo SITC Nivel 3 tenga tres números

    comercio = comercio[comercio['SITC Nivel 3'].str.len() == 3]

# 22. Creamos las columnas SITC Nivel 1 y SITC Nivel 2 a partir de SITC Nivel 3

    sitcSeparado = comercio["SITC Nivel 3"].str.split("", expand=True, n = 3)
    sitcNivelUno = sitcSeparado[[1]]
    sitcNivelUno.columns = ['SITC Nivel 1']
    sitcNivelDos = sitcSeparado[1] + sitcSeparado[2]
    sitcNivelDos = pd.DataFrame(sitcNivelDos)
    sitcNivelDos.columns = ['SITC Nivel 2']
    comercio = pd.merge(comercio, sitcNivelUno, left_index=True, right_index=True)
    comercio = pd.merge(comercio, sitcNivelDos, left_index=True, right_index=True)

# 23. Ordenamos las columnas

    first_column = comercio.pop('SITC Nivel 2')
    comercio.insert(0, 'SITC Nivel 2', first_column)
    first_column = comercio.pop('SITC Nivel 1')
    comercio.insert(0, 'SITC Nivel 1', first_column)
    return comercio

# 24. Se crea un archivo con nombre ProductoPaisImp.csv que recoge el producto más importado desde cada país del top diez de los que más se importa
def crearListaProductoPaisImp(comercio2021):
    productoPaisImp = comercio2021[comercio2021["Países"].isin(['Germany', "China", 'Belgium', "United States", "United Kingdom", 'France', 'Italy', "Russia", "Poland", 'Spain'])]
    productoPaisImp = productoPaisImp.groupby(["Países", "Producto"]).sum()['Importaciones (millones de €)'].sort_values(ascending=False)
    productoPaisImp = productoPaisImp.reset_index()
    productoGermanyImp = productoPaisImp[productoPaisImp["Países"] == "Germany"]
    productoGermanyImp = productoGermanyImp.head(1)
    productoChinaImp = productoPaisImp[productoPaisImp["Países"] == "China"]
    productoChinaImp = productoChinaImp.head(1)
    productoBelgiumImp = productoPaisImp[productoPaisImp["Países"] == "Belgium"]
    productoBelgiumImp = productoBelgiumImp.head(1)
    productoUnitedStatesImp = productoPaisImp[productoPaisImp["Países"] == "United States"]
    productoUnitedStatesImp = productoUnitedStatesImp.head(1)
    productoUnitedKingdomImp = productoPaisImp[productoPaisImp["Países"] == "United Kingdom"]
    productoUnitedKingdomImp = productoUnitedKingdomImp.head(1)
    productoFranceImp = productoPaisImp[productoPaisImp["Países"] == "France"]
    productoFranceImp = productoFranceImp.head(1)
    productoItalyImp = productoPaisImp[productoPaisImp["Países"] == "Italy"]
    productoItalyImp = productoItalyImp.head(1)
    productoRussiaImp = productoPaisImp[productoPaisImp["Países"] == "Russia"]
    productoRussiaImp = productoRussiaImp.head(1)
    productoPolandImp = productoPaisImp[productoPaisImp["Países"] == "Poland"]
    productoPolandImp = productoPolandImp.head(1)
    productoSpainImp = productoPaisImp[productoPaisImp["Países"] == "Spain"]
    productoSpainImp = productoSpainImp.head(1)
    productoPaisesImp = pd.concat([productoGermanyImp, productoChinaImp, productoBelgiumImp, productoUnitedStatesImp, productoUnitedKingdomImp, productoFranceImp, productoItalyImp, productoRussiaImp, productoPolandImp, productoSpainImp])
    productoPaisesImp = productoPaisesImp.set_index("Países")
    productoPaisesImp.to_csv("data/dataAfterCleaning/ProductoPaisImp.csv")

# 25. Se crea un archivo con nombre ProductoPaisExp.csv que recoge el producto más exportado a cada país del top diez a los que más se exporta
def crearListaProductoPaisExp(comercio2021):    
    productoPaisExp = comercio2021[comercio2021["Países"].isin(['Germany', 'Belgium', 'France', "United Kingdom", "United States", 'Italy', 'Spain', "Poland", "China", "Sweden"])]
    productoPaisExp = productoPaisExp.groupby(["Países", "Producto"]).sum()['Exportaciones (millones de €)'].sort_values(ascending=False)
    productoPaisExp = productoPaisExp.reset_index()
    productoGermanyExp = productoPaisExp[productoPaisExp["Países"] == "Germany"]
    productoGermanyExp = productoGermanyExp.head(1)
    productoBelgiumExp = productoPaisExp[productoPaisExp["Países"] == "Belgium"]
    productoBelgiumExp = productoBelgiumExp.head(1)
    productoFranceExp = productoPaisExp[productoPaisExp["Países"] == "France"]
    productoFranceExp = productoFranceExp.head(1)
    productoUnitedKingdomExp = productoPaisExp[productoPaisExp["Países"] == "United Kingdom"]
    productoUnitedKingdomExp = productoUnitedKingdomExp.head(1)
    productoUnitedStatesExp = productoPaisExp[productoPaisExp["Países"] == "United States"]
    productoUnitedStatesExp = productoUnitedStatesExp.head(1)
    productoItalyExp = productoPaisExp[productoPaisExp["Países"] == "Italy"]
    productoItalyExp = productoItalyExp.head(1)
    productoSpainExp = productoPaisExp[productoPaisExp["Países"] == "Spain"]
    productoSpainExp = productoSpainExp.head(1)
    productoPolandExp = productoPaisExp[productoPaisExp["Países"] == "Poland"]
    productoPolandExp = productoPolandExp.head(1)
    productoChinaExp = productoPaisExp[productoPaisExp["Países"] == "China"]
    productoChinaExp = productoChinaExp.head(1)
    productoSwedenExp = productoPaisExp[productoPaisExp["Países"] == "Sweden"]
    productoSwedenExp = productoSwedenExp.head(1)
    productoPaisesExp = pd.concat([productoGermanyExp, productoBelgiumExp, productoFranceExp, productoUnitedKingdomExp, productoUnitedStatesExp, productoItalyExp, productoSpainExp, productoPolandExp, productoChinaExp, productoSwedenExp])
    productoPaisesExp = productoPaisesExp.set_index("Países")
    productoPaisesExp.to_csv("data/dataAfterCleaning/ProductoPaisExp.csv")

# 26. Se crea un archivo con nombre Globo2021.csv que recoge los países, sus importaciones, sus exportaciones, sus latitudes y sus altitudes
def crearGlobo(comercio2021, coordenadas):
    comercioGlobo2021 = comercio2021.groupby("Países").sum().iloc[::, 4:8:]
    comercioGlobo2021["Año"] = 2021
    comercioGlobo2021 = comercioGlobo2021.reset_index()
    globo2021 = pd.merge(comercioGlobo2021, coordenadas)
    globo2021.to_csv("data/dataAfterCleaning/Globo2021.csv")