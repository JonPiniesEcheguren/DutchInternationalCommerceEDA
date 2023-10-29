import pandas as pd

# 1. Importar datasets de comercio exterior para cada año

data2021 = pd.read_csv("data/dataBeforeCleaning/Data2021.csv", sep=";")
data2020 = pd.read_csv("data/dataBeforeCleaning/Data2020.csv", sep=";")
data2019 = pd.read_csv("data/dataBeforeCleaning/Data2019.csv", sep=";")
data2018 = pd.read_csv("data/dataBeforeCleaning/Data2018.csv", sep=";")
data2017 = pd.read_csv("data/dataBeforeCleaning/Data2017.csv", sep=";")
data2016 = pd.read_csv("data/dataBeforeCleaning/Data2016.csv", sep=";")
data2015 = pd.read_csv("data/dataBeforeCleaning/Data2015.csv", sep=";")
data2014 = pd.read_csv("data/dataBeforeCleaning/Data2014.csv", sep=";")
data2013 = pd.read_csv("data/dataBeforeCleaning/Data2013.csv", sep=";")
data2012 = pd.read_csv("data/dataBeforeCleaning/Data2012.csv", sep=";")

# 2. Importar dataset de relación código SITC - nombre producto

metadataSITC = pd.read_csv("data/dataBeforeCleaning/MetadataSITC.csv", sep=";", encoding='latin-1')

# 3. Importar dataset de relación código país - nombre país

metadataCountries = pd.read_csv("data/dataBeforeCleaning/MetadataCountries.csv", sep=";", encoding='latin-1')

# 4. Importar dataset Coordenadas.csv

coordenadas = pd.read_csv("data/dataBeforeCleaning/Coordenadas.csv", sep=";", encoding='latin-1')