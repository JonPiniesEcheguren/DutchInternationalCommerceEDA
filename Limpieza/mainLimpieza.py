import pandas as pd
import functionsLimpieza as fu
import variablesLimpieza as va

# LIMPIEZA DE DATOS
# 1. Primera limpieza de cada dataset data20xx. Devuelve el dataset modificado. Detalle de la limpieza en funciones.py
# 2. Se asigna el año correspondiente a cada data20xx modificado
# 3. Segunda y última limpieza de cada dataset data20xx. Devuelve el dataset totalmente depurado. Detalle de la limpieza en funciones.py
#2021
dataset2021 = fu.LimpiezaDatasetInicial(va.metadataSITC, va.metadataCountries, va.data2021)
dataset2021["Año"] = 2021
comercio2021 = fu.LimpiezaDatasetPosterior(dataset2021)
comercio2021.to_csv("data/dataAfterCleaning/Comercio2021.csv")
#2020
dataset2020 = fu.LimpiezaDatasetInicial(va.metadataSITC, va.metadataCountries, va.data2020)
dataset2020["Año"] = 2020
comercio2020 = fu.LimpiezaDatasetPosterior(dataset2020)
#2019
dataset2019 = fu.LimpiezaDatasetInicial(va.metadataSITC, va.metadataCountries, va.data2019)
dataset2019["Año"] = 2019
comercio2019 = fu.LimpiezaDatasetPosterior(dataset2019)
#2018
dataset2018 = fu.LimpiezaDatasetInicial(va.metadataSITC, va.metadataCountries, va.data2018)
dataset2018["Año"] = 2018
comercio2018 = fu.LimpiezaDatasetPosterior(dataset2018)
#2017
dataset2017 = fu.LimpiezaDatasetInicial(va.metadataSITC, va.metadataCountries, va.data2017)
dataset2017["Año"] = 2017
comercio2017 = fu.LimpiezaDatasetPosterior(dataset2017)
#2016
dataset2016 = fu.LimpiezaDatasetInicial(va.metadataSITC, va.metadataCountries, va.data2016)
dataset2016["Año"] = 2016
comercio2016 = fu.LimpiezaDatasetPosterior(dataset2016)
#2015
dataset2015 = fu.LimpiezaDatasetInicial(va.metadataSITC, va.metadataCountries, va.data2015)
dataset2015["Año"] = 2015
comercio2015 = fu.LimpiezaDatasetPosterior(dataset2015)
#2014
dataset2014 = fu.LimpiezaDatasetInicial(va.metadataSITC, va.metadataCountries, va.data2014)
dataset2014["Año"] = 2014
comercio2014 = fu.LimpiezaDatasetPosterior(dataset2014)
#2013
dataset2013 = fu.LimpiezaDatasetInicial(va.metadataSITC, va.metadataCountries, va.data2013)
dataset2013["Año"] = 2013
comercio2013 = fu.LimpiezaDatasetPosterior(dataset2013)
#2012
dataset2012 = fu.LimpiezaDatasetInicial(va.metadataSITC, va.metadataCountries, va.data2012)
dataset2012["Año"] = 2012
comercio2012 = fu.LimpiezaDatasetPosterior(dataset2012)

# 4. Se concatenan en un mismo dataset llamado comercio todos los datasets comercio20xx. Se guarda en un arhivo .csv llamado comercio.csv
comercio = pd.concat([comercio2021, comercio2020, comercio2019, comercio2018, comercio2017, comercio2016, comercio2015, comercio2014, comercio2013, comercio2012], ignore_index=True)
comercio.to_csv("data/dataAfterCleaning/Comercio.csv")

# 5. Se crea un archivo con nombre ProductoPaisImp.csv que recoge el producto más importado a cada país del top diez a los que más se importa
fu.crearListaProductoPaisImp(comercio2021)

# 6. Se crea un archivo con nombre ProductoPaisExp.csv que recoge el producto más exportado a cada país del top diez a los que más se exporta
fu.crearListaProductoPaisExp(comercio2021)

# 7. Se crea un archivo con nombre Globo2021.csv que recoge los países, sus importaciones, sus exportaciones, sus latitudes y sus altitudes
fu.crearGlobo(comercio2021, va.coordenadas)