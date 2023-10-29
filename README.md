# Dutch International Commerce EDA

Publicado en Streamlit App 👉 [Comercio Exterior en Países Bajos · Streamlit](https://dutchinternationalcommerceeda.streamlit.app/)

El presente *Exploratory Data Analysis* analiza los datos aportados por Centraal Bureau van Statistiek (CBS) sobre el comercio exterior de bienes neerlandés. Para ello, se ha accedido a la base de datos de CBS y recopilado las exportaciones, importaciones, países de origen, países de destino y categorías de producto (código SITC) para cada año en el periodo 2012-2021 (datos completos disponibles más recientes). De esta manera, este trabajo determina los socios comerciales más importantes, los productos más comercializados y las tendencias en los últimos diez años.

Cabe destacar que el objetivo de este trabajo ha sido poner en práctica habilidades y herramientas técnicas como la limpieza de datos, las librerías de visualización y el análisis de datos. A pesar de no tener el foco principal en la profundidad del análisis, este trabajo ha procurado ser riguroso con las conclusiones extraídas.

Este trabajo ha necesitado tres procesos diferentes:

1. Limpieza de datos
2. Creación de visualizaciones
3. Creación de la aplicación en Streamlit

# Contenido del repositorio

El repositorio consta de:

- Carpeta "data": 

  Contiene todos los datos necesarios para el EDA.

  - Carpeta "dataBeforeCleaning":
    - Contiene 13 archivos .csv. Estos archivos han sido obtenidos desde la fuente CBS. Los archivos fueron mínimamente modificados en Microsoft Excel previamente, pero su aspecto original era muy parecido al actual. Estos archivos necesitan una "limpieza" para poder ser utilizados en un análisis.

  - Carpeta "dataAfterCleaning":
    - Contiene 5 archivos .csv y 1 archivo .xlsx. Estos archivos han sido generados partiendo de los datasets descargados desde CBS. Tras un proceso de "limpieza", estos archivos ya están preparados para poder ser utilizados para un análisis. 

- Carpeta "Limpieza":

  Contiene toda la parte del trabajo dedicada a la "limpieza" de datos. Constituye por sí mismo un programa independiente. 

  - Archivo "variablesLimpieza.py": 

    Mediante este archivo cargamos todos los archivos de datos de la carpeta "dataBeforeCleaning" al programa "mainLimpieza.py". 

  - Archivo "functionsLimpieza.py": 

    Contiene todas las funciones que transformarán los archivos "sin limpiar" a archivos listos para ser analizados.

  - Archivo "mainLimpieza.py":

    El main del apartado limpieza llama a variables y functions, y ejecuta el programa. Crea los archivos de datos de la carpeta "dataAfterCleaning".

- Archivo "variables.py":

  Mediante este archivo cargamos todos los archivos de datos de la carpeta "dataAfterCleaning" al programa "main.py".  

- Archivo "functions.py":

  Contiene dos tipos de funciones. Un primer grupo de funciones será el encargado de crear las visualizaciones que se han utilizado para el análisis. El segundo grupo de funciones será el encargado de configurar cada apartado de la página de Streamlit. Estas segundas funciones llamarán a las primeras para mostrar en Streamlit las visualizaciones creadas.

- Archivo "main.py":

  El main llama a variables y functions, y ejecuta el programa. Crea la página de Streamlit y los apartados que tendrá.

- Carpeta "images":

  Contiene tres archivos .jpg que se mostrarán en Streamlit.

- Archivo "memoria.ipynb":

  La memoria es un resumen explicativo de cada proceso seguido en este proyecto. Contiene, haciendo uso de datasets de dos únicos años para su mejor comprensión, cada uno de los pasos realizados. Cada paso contiene una explicación y muestra al usuario de forma visual la acción realizada. Se muestra todo el proceso desde los archivos de datos "sin limpiar" hasta la creación de visualizaciones. La última parte del proceso (Integrar las visualizaciones en Streamlit) no esta explicado en la memoria.  

- Otros: .gitignore, README.md y requirements.txt 

### Instrucciones de instalación:

- Clonar el repositorio:

  - `git clone https://github.com/JonPiniesEcheguren/DutchInternationalCommerceEDA.git` 

- Crear y activar el entorno virtual:

  - Versión Python 3.11.2

  - Windows

    - `python -m venv env` 
    - `env\scripts\activate.bat` (Windows command line)
    - `env\scripts\activate.ps1` (Windows PowerShell)

  - MacOs / Linux

    - `python3 -m venv env`

    - `source env/bin/activate`

- Instalar las librerias
  - `pip install -r requirements.txt`

- Instrucciones de ejecución
  - `py mainLimpieza.py`
  - `py main.py`

# Autor

- Jon Pinies Echeguren
