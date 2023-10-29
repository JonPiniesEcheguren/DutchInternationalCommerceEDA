# 1. Importamos librerías Pandas y Numpy
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import seaborn as sns
import folium
from folium import plugins
import squarify
import matplotlib.pyplot as plt
import plotly.express as px
from io import BytesIO 

# CREACION DE LAS FIGURAS EN FUNCIONES
# 1. Creación de un globo interactivo para mostrar las importaciones desde Países Bajos en 2021 a cada país, con nombre de los países
def globoImpPaises(globo2021):
    fig_orth_2 = px.scatter_geo(globo2021, lon='Longitude', lat='Latitude',
                            hover_name='Importaciones (millones de €)', 
                            size='Importaciones (millones de €)', 
                            text='Países',
                            projection="orthographic"
                            )
    return fig_orth_2

# 2. Creación de un globo interactivo para mostrar las importaciones desde Países Bajos en 2021 a cada país, sin nombre de los países
def globoImpSinPaises(globo2021):
    fig_orth_3 = px.scatter_geo(globo2021, lon='Longitude', lat='Latitude',
                            hover_name='Importaciones (millones de €)', 
                            size='Importaciones (millones de €)', 
                            projection="orthographic"
                            )
    return fig_orth_3
    
# 3. Creación de un globo interactivo para mostrar las exportaciones desde Países Bajos en 2021 a cada país, con nombre de los países
def globoExpPaises(globo2021):
    fig_orth = px.scatter_geo(globo2021, lon='Longitude', lat='Latitude',
                            hover_name='Exportaciones (millones de €)', 
                            size='Exportaciones (millones de €)', 
                            text='Países',
                            projection="orthographic"
                            )
    return fig_orth

# 4. Creación de un globo interactivo para mostrar las exportaciones desde Países Bajos en 2021 a cada país, sin nombre de los países
def globoExpSinPaises(globo2021):
    fig_orth_1 = px.scatter_geo(globo2021, lon='Longitude', lat='Latitude',
                                hover_name='Exportaciones (millones de €)', 
                                size='Exportaciones (millones de €)',
                                projection="orthographic"
                                )
    return fig_orth_1

# 5. Creación de un mapa interactivo que muestra los diez países de los que más se importa bienes a Países Bajos y los valores
def mapaInteractivoImp(comercio2021):
# 5.a. Creación de variables
    comercioImpMap = comercio2021[["Países", "Importaciones (millones de €)"]].groupby("Países").sum().sort_values(by="Importaciones (millones de €)", ascending= False).head(10)
    paisesImpMap = list(comercioImpMap.index)
    importacionesMap = list(comercioImpMap["Importaciones (millones de €)"])

    cm_enum_df = pd.DataFrame({'country': paisesImpMap,
                            'importaciones': importacionesMap,
                            'latitude': [51.165691, 35.86166, 50.503887, 37.09024, 55.378051, 46.227638, 41.87194, 61.52401, 51.919438, 40.463667],
                            'longitude': [10.451526, 104.195397, 4.469936, -95.712891, -3.435973, 2.213749, 12.56738, 105.318756, 19.145136, -3.74922],
                            'icon_num': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
# 5.b. Mapa
    map_imp = folium.Map([30, 0], zoom_start=3)
# 5.c. Iconos usando plugins.BeautifyIcon
    for i in cm_enum_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                    popup=i.importaciones,
                    icon=plugins.BeautifyIcon(number=i.icon_num,
                                                border_color='blue',
                                                border_width=1,
                                                text_color='red',
                                                inner_icon_style='margin-top:0px;')).add_to(map_imp)
# 5.d. Devolver mapa    
    return map_imp

# 6. Creación de un mapa interactivo que muestra los diez países de los que más se exporta bienes a Países Bajos y los valores
def mapaInteractivoExp(comercio2021):
# 6.a. Creación de variables
    comercioExpMap = comercio2021[["Países", "Exportaciones (millones de €)"]].groupby("Países").sum().sort_values(by="Exportaciones (millones de €)", ascending= False).head(10)
    paisesExpMap = list(comercioExpMap.index)
    exportacionesMap = list(comercioExpMap["Exportaciones (millones de €)"])

    cm_enum_df = pd.DataFrame({'country': paisesExpMap,
                            'exportaciones': exportacionesMap,
                            'latitude': [51.165691, 50.503887, 46.227638, 55.378051, 37.09024, 41.87194, 40.463667, 51.919438, 35.86166, 60.128161],
                            'longitude': [10.451526, 4.469936, 2.213749, -3.435973, -95.712891, 12.56738, -3.74922, 19.145136, 104.195397, 18.643501],
                            'icon_num': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
# 6.b. Mapa
    map_exp = folium.Map([30, 0], zoom_start=3)

# 6.c. Iconos usando plugins.BeautifyIcon
    for i in cm_enum_df.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                    popup=i.exportaciones,
                    icon=plugins.BeautifyIcon(number=i.icon_num,
                                                border_color='blue',
                                                border_width=1,
                                                text_color='red',
                                                inner_icon_style='margin-top:0px;')).add_to(map_exp)
# 6.d. Devolver mapa    
    return map_exp

# 7. Creación de un treemap para mostrar los primeros 32 países de destino de las importaciones de bienes desde Países Bajos en 2021
def treemapImp(comercio2021):
    data = comercio2021.groupby("Países").sum()['Importaciones (millones de €)'].sort_values(ascending=False)[:32]
    treemapImpFig = plt.figure(figsize=(8,6))
    squarify.plot(sizes=data.values, label=data.index, alpha=.8, text_kwargs={'fontsize':6}, color = sns.light_palette("seagreen", len(data.values)))
    plt.axis('off')
    return treemapImpFig

# 8. Creación de un treemap para mostrar los primeros 32 países de destino de las exportaciones de bienes desde Países Bajos en 2021
def treemapExp(comercio2021):
    data = comercio2021.groupby("Países").sum()['Exportaciones (millones de €)'].sort_values(ascending=False)[:32]
    treemapExpFig = plt.figure(figsize=(8,6))
    squarify.plot(sizes=data.values, label=data.index, alpha=.8, text_kwargs={'fontsize':6}, color = sns.light_palette("seagreen", len(data.values)))
    plt.axis('off')
    return treemapExpFig

# 9. Creación de un lollipop para mostrar las importaciones en 2021 por categorías de producto (SITC Nivel 1)
def lollipopImp1(comercio2021, sitc):
    sitc1 = sitc.rename(columns={"SITC": "SITC Nivel 1"})
    comercio2021["SITC Nivel 1"] = comercio2021["SITC Nivel 1"].astype(str)
    lollipopImp1 = comercio2021.groupby("SITC Nivel 1")[["Importaciones (millones de €)"]].sum()
    lollipopImp1 = lollipopImp1.reset_index()
    lollipopMergeImp1 = pd.merge(sitc1, lollipopImp1)
    lollipopMergeImp1 = lollipopMergeImp1.drop(columns="SITC Nivel 1")
    lollipopMergeImp1 = lollipopMergeImp1.set_index("Producto")
    lollipopMergeImp1 = lollipopMergeImp1.sort_values(by="Importaciones (millones de €)", ascending=False)
    lolliImp1 = plt.figure(figsize=(10,5))
    plt.hlines(y=lollipopMergeImp1.index,
        xmin=150,
        xmax=lollipopMergeImp1,
        color='skyblue')
    plt.plot(lollipopMergeImp1, lollipopMergeImp1.index, "o");
    return lolliImp1

# 10. Creación de un lollipop para mostrar las exportaciones en 2021 por categorías de producto (SITC Nivel 1)
def lollipopExp1(comercio2021, sitc):
    sitc1 = sitc.rename(columns={"SITC": "SITC Nivel 1"})
    comercio2021["SITC Nivel 1"] = comercio2021["SITC Nivel 1"].astype(str)
    lollipopExp1 = comercio2021.groupby("SITC Nivel 1")[["Exportaciones (millones de €)"]].sum()
    lollipopExp1 = lollipopExp1.reset_index()
    lollipopMergeExp1 = pd.merge(sitc1, lollipopExp1)
    lollipopMergeExp1 = lollipopMergeExp1.drop(columns="SITC Nivel 1")
    lollipopMergeExp1 = lollipopMergeExp1.set_index("Producto")
    lollipopMergeExp1 = lollipopMergeExp1.sort_values(by="Exportaciones (millones de €)", ascending=False)
    lolliExp1 = plt.figure(figsize=(10,5))
    plt.hlines(y=lollipopMergeExp1.index,
        xmin=150,
        xmax=lollipopMergeExp1,
        color='skyblue')
    plt.plot(lollipopMergeExp1, lollipopMergeExp1.index, "o");
    return lolliExp1

# 11. Creación de un lollipop para mostrar las importaciones en 2021 por categorías de producto (SITC Nivel 2)
def lollipopImp2(comercio2021, sitc):
    sitc2 = sitc.rename(columns={"SITC": "SITC Nivel 2"})
    comercio2021["SITC Nivel 2"] = comercio2021["SITC Nivel 2"].astype(str)
    lollipopImp2 = comercio2021.groupby("SITC Nivel 2")[["Importaciones (millones de €)"]].sum()
    lollipopImp2 = lollipopImp2.reset_index()
    lollipopMergeImp2 = pd.merge(sitc2, lollipopImp2)
    lollipopMergeImp2 = lollipopMergeImp2.drop(columns="SITC Nivel 2")
    lollipopMergeImp2 = lollipopMergeImp2.set_index("Producto")
    lollipopMergeImp2 = lollipopMergeImp2.sort_values(by="Importaciones (millones de €)", ascending=False)
    lollipopMergeImp2Head = lollipopMergeImp2.head(10)
    lolliImp2 = plt.figure(figsize=(10,5))
    plt.hlines(y=lollipopMergeImp2Head.index,
        xmin=150,
        xmax=lollipopMergeImp2Head,
        color='skyblue')
    plt.plot(lollipopMergeImp2Head, lollipopMergeImp2Head.index, "o");
    return lolliImp2

# 12. Creación de un lollipop para mostrar las exportaciones en 2021 por categorías de producto (SITC Nivel 2)
def lollipopExp2(comercio2021, sitc):
    sitc2 = sitc.rename(columns={"SITC": "SITC Nivel 2"})
    comercio2021["SITC Nivel 2"] = comercio2021["SITC Nivel 2"].astype(str)
    lollipopExp2 = comercio2021.groupby("SITC Nivel 2")[["Exportaciones (millones de €)"]].sum()
    lollipopExp2 = lollipopExp2.reset_index()
    lollipopMergeExp2 = pd.merge(sitc2, lollipopExp2)
    lollipopMergeExp2 = lollipopMergeExp2.drop(columns="SITC Nivel 2")
    lollipopMergeExp2 = lollipopMergeExp2.set_index("Producto")
    lollipopMergeExp2 = lollipopMergeExp2.sort_values(by="Exportaciones (millones de €)", ascending=False)
    lollipopMergeExp2Head = lollipopMergeExp2.head(10)
    lolliExp2 = plt.figure(figsize=(10,5))
    plt.hlines(y=lollipopMergeExp2Head.index,
        xmin=150,
        xmax=lollipopMergeExp2Head,
        color='skyblue')
    plt.plot(lollipopMergeExp2Head, lollipopMergeExp2Head.index, "o");
    return lolliExp2

# 13. Creación de un lollipop para mostrar las importaciones en 2021 por categorías de producto (SITC Nivel 3)
def lollipopImp3(comercio2021, sitc):
    sitc3 = sitc.rename(columns={"SITC": "SITC Nivel 3"})
    comercio2021["SITC Nivel 3"] = comercio2021["SITC Nivel 3"].astype(str)
    lollipopImp3 = comercio2021.groupby("SITC Nivel 3")[["Importaciones (millones de €)"]].sum()
    lollipopImp3 = lollipopImp3.reset_index()
    lollipopMergeImp3 = pd.merge(sitc3, lollipopImp3)
    lollipopMergeImp3 = lollipopMergeImp3.drop(columns="SITC Nivel 3")
    lollipopMergeImp3 = lollipopMergeImp3.set_index("Producto")
    lollipopMergeImp3 = lollipopMergeImp3.sort_values(by="Importaciones (millones de €)", ascending=False)
    lollipopMergeImp3Head = lollipopMergeImp3.head(10)
    lolliImp3 = plt.figure(figsize=(10,5))
    plt.hlines(y=lollipopMergeImp3Head.index,
        xmin=150,
        xmax=lollipopMergeImp3Head,
        color='skyblue')
    plt.plot(lollipopMergeImp3Head, lollipopMergeImp3Head.index, "o");
    return lolliImp3

# 14. Creación de un lollipop para mostrar las exportaciones en 2021 por categorías de producto (SITC Nivel 3)
def lollipopExp3(comercio2021, sitc):
    sitc3 = sitc.rename(columns={"SITC": "SITC Nivel 3"})
    comercio2021["SITC Nivel 3"] = comercio2021["SITC Nivel 3"].astype(str)
    lollipopExp3 = comercio2021.groupby("SITC Nivel 3")[["Exportaciones (millones de €)"]].sum()
    lollipopExp3 = lollipopExp3.reset_index()
    lollipopMergeExp3 = pd.merge(sitc3, lollipopExp3)
    lollipopMergeExp3 = lollipopMergeExp3.drop(columns="SITC Nivel 3")
    lollipopMergeExp3 = lollipopMergeExp3.set_index("Producto")
    lollipopMergeExp3 = lollipopMergeExp3.sort_values(by="Exportaciones (millones de €)", ascending=False)
    lollipopMergeExp3Head = lollipopMergeExp3.head(10)
    lolliExp3 = plt.figure(figsize=(10,5))
    plt.hlines(y=lollipopMergeExp3Head.index,
        xmin=150,
        xmax=lollipopMergeExp3Head,
        color='skyblue')
    plt.plot(lollipopMergeExp3Head, lollipopMergeExp3Head.index, "o");
    return lolliExp3

# 15. Creación de un Barplot para mostrar las importaciones en los últimos diez años (2012-2021)
def barplotImp(comercio):
    comercioBarplot = comercio[["Importaciones (millones de €)", "Año"]].groupby("Año").sum()
    comercioImpFigura = plt.figure(figsize=(20,8))
    sns.barplot(hue="Año",
                y="Importaciones (millones de €)",
                data=comercioBarplot,
                palette="Blues_d",
                legend="full",
                errorbar=None);
    comercioImpFiguraImg = BytesIO()
    comercioImpFigura.savefig(comercioImpFiguraImg, format='png')
    comercioImpFiguraImg.seek(0)
    return comercioImpFiguraImg

# 16. Creación de un Barplot para mostrar las exportaciones en los últimos diez años (2012-2021)
def barplotExp(comercio):
    comercioBarplot = comercio[["Exportaciones (millones de €)", "Año"]].groupby("Año").sum()
    comercioExpFigura = plt.figure(figsize=(20,8))
    sns.barplot(hue="Año",
                y="Exportaciones (millones de €)",
                data=comercioBarplot,
                palette="Blues_d",
                legend="full",
                errorbar=None);
    comercioExpFiguraImg = BytesIO()
    comercioExpFigura.savefig(comercioExpFiguraImg, format='png')
    comercioExpFiguraImg.seek(0)
    return comercioExpFiguraImg

# 17. Creación de una time series para representar la variación de las importaciones en el tiempo para cada uno de los países en el top 10
def timeseriesImp(comercio):
    comercioTimeseries = comercio[comercio['Países'].isin(['Germany', "China", 'Belgium', "United States", "United Kingdom", 'France', 'Italy', "Russia", "Poland", 'Spain'])]
    comercioTimeseries = comercioTimeseries.groupby(['Países', 'Año']).sum()
    comercioTimeseries.reset_index(inplace=True)
    timeseriesImpFig = plt.figure(figsize=(10,10))
    sns.lineplot(data=comercioTimeseries,
                x="Año",
                y="Importaciones (millones de €)",
                hue="Países",
                legend='full',
                linewidth = 3);
    plt.legend (loc= "upper left")
    timeseriesImpFigImg = BytesIO()
    timeseriesImpFig.savefig(timeseriesImpFigImg, format='png')
    timeseriesImpFigImg.seek(0)
    return timeseriesImpFigImg

# 18. Creación de una time series para representar la variación de las exportaciones en el tiempo para cada uno de los países en el top 10
def timeseriesExp(comercio):
    comercioTimeseries = comercio[comercio['Países'].isin(['Germany', 'Belgium', 'France', "United Kingdom", "United States", 'Italy', 'Spain', "Poland", "China", "Sweden"])]
    comercioTimeseries = comercioTimeseries.groupby(['Países', 'Año']).sum()
    comercioTimeseries.reset_index(inplace=True)
    timeseriesExpFig = plt.figure(figsize=(10,10))
    sns.lineplot(data=comercioTimeseries,
                x="Año",
                y="Exportaciones (millones de €)",
                hue="Países",
                linewidth = 3);
    plt.legend (loc= "upper left")
    timeseriesExpFigImg = BytesIO()
    timeseriesExpFig.savefig(timeseriesExpFigImg, format='png')
    timeseriesExpFigImg.seek(0)
    return timeseriesExpFigImg

# STREAMLIT, CREACION DE APARTADOS
# 19. Creación del apartado Inicio de Streamlit
def inicio():

    st.title('El comercio exterior de bienes en Países Bajos')
    st.subheader('Análisis exploratorio de datos \n Fuente: Centraal Bureau van Statistiek (CBS), Instituto nacional de estadística neerlandés \n\n\n Elaborado por Jon Pinies Echeguren')
    st.image('images/amsterdam_canal.jpg', caption='Países Bajos fue el cuarto mayor exportador y décimo mayor importador del mundo en 2022')
    st.markdown('El presente informe analiza los datos aportados por Centraal Bureau van Statistiek (CBS) sobre el comercio exterior de bienes \
            neerlandés. Para ello, se ha accedido a la base de datos de CBS y recopilado las exportaciones, importaciones, países de origen, \
            países de destino y categorías de producto (código SITC) para cada año en el periodo 2012-2021 (datos completos disponibles más \
            recientes). De esta manera, este trabajo determina los socios comerciales más importantes, los productos más comercializados y \
            las tendencias en los últimos diez años.')
    st.write('Los datos recopilados en CBS pueden no coincidir con otras bases de datos pues cada fuente hace uso de una metodología de \
        obtención de datos diferente. Además, los datos totales han sido calculados mediante la suma de los datos por producto. Esto hace \
        diferir mínimamente los valores totales utilizados en este trabajo respecto a los otorgados por CBS que no sigue este principio.') 
    st.markdown('Cabe destacar que el objetivo de este trabajo ha sido poner en práctica habilidades y \
            herramientas técnicas como la limpieza de datos, las librerías de visualización y el análisis de datos. A pesar de no tener \
            el foco principal en la profundidad del análisis, este trabajo ha procurado ser riguroso con las conclusiones extraídas.')
    st.subheader('Herramienta para la internacionalización')
    st.markdown('La aplicabilidad de una solución como esta en la vida real es alta. Las empresas españolas con interés en expandir su negocio \
            a través del comercio internacional acuden frecuentemente a expertos en la materia para recibir servicios de consultoría. ICEX, \
            entidad pública que tiene como misión promover la internacionalización de las empresas españolas y la promoción de la inversión \
            extranjera, elabora numerosos informes comerciales sobre una mayoría de países y sectores.')
    st.markdown('Como complemento a dichos informes, las empresas españolas podrían tener acceso a una aplicación interactiva que les permitiese \
            personalizar búsquedas. De esta manera, las empresas podrían acceder de manera ágil y visual a toda la información requerida desde \
            un mismo lugar.')
    st.markdown('Una aplicación real útil debería escalar los apartados de este trabajo a todos los países, analizar cada sector con \
            profundidad, añadir variables propias de cada sector y país... Tal y como comentaba anteriormente, este trabajo tiene como único \
            objetivo poner en práctica los conocimientos de Data Analysis adquiridos.')
    
# 20. Creación del apartado Visión general de Streamlit
def visionGeneral(globo2021):
    
    st.title('Una mirada al mundo')
    st.subheader('Diferencias entre países')
    st.markdown('La fortaleza del comercio exterior de un país está determinada por una compleja interacción de factores. Las políticas \
            comerciales y la estabilidad política y económica proporcionan el marco necesario para el intercambio de bienes y servicios. \
            Una infraestructura y logística eficientes facilitan la movilidad de mercancías, reduciendo costos. La capacidad productiva, \
            apoyada por una fuerza laboral capacitada, impulsa la competitividad. Los recursos naturales y la tecnología influyen en la \
            diversificación de productos. El tipo de cambio y el acceso a mercados extranjeros son vitales para la expansión internacional.')
    st.markdown('En cuanto a las relaciones comerciales entre dos países, estas se fundamentan en la explotación de ventajas comparativas, \
            la existencia de acuerdos comerciales y un entorno legal que proteja los derechos de propiedad y haga cumplir los contratos. La \
            comprensión y respeto por las diferencias culturales y lingüísticas, así como el acceso a mercados y la colaboración en temas \
            globales, también juegan un papel crucial.')
    st.markdown('La concentración de las exportaciones e importaciones neerlandesas en el continente europeo es notable. Una ubicación \
            geográfica estratégica en el corazón de Europa, una infraestructura de transporte avanzada,  poseer el principal puerto europeo \
            (Róterdam) y el mercado único europeo son algunas de las razones que explican esta alta proporción. Lejos de Europa, Estados \
            Unidos y China, principales actores comerciales globales, son los socios más relevantes.')
    
    eleccion = st.radio(label='Veamos las exportaciones e importaciones de bienes (en millones de €) de Países Bajos en 2021 por país:', options=('Exportaciones', 'Importaciones'))
    
    if eleccion == 'Exportaciones':

        bar_orth = st.checkbox('Incluir nombres de los países sobre el mapa')
        
        if bar_orth:
            fig_orth = globoExpPaises(globo2021)
            st.plotly_chart(fig_orth)
        
        else:
            fig_orth1 = globoExpSinPaises(globo2021)
            st.plotly_chart(fig_orth1)

        with st.expander('Descripción'):
            st.write('En este mapa se pueden apreciar las exportaciones (en millones de €) de bienes desde Países Bajos en 2021 por país. \
                El tamaño de cada burbuja está en proporción al volumen de la exportación.')

    if eleccion == 'Importaciones':

        bar_orth = st.checkbox('Incluir nombres de los países sobre el mapa')
        
        if bar_orth:
            fig_orth2 = globoImpPaises(globo2021)
            st.plotly_chart(fig_orth2)
        
        else:
            fig_orth3 = globoImpSinPaises(globo2021)
            st.plotly_chart(fig_orth3)

        with st.expander('Descripción'):
            st.write('En este mapa se pueden apreciar las importaciones (en millones de €) de bienes a Países Bajos en 2021 por país. El \
                tamaño de cada burbuja está en proporción al volumen de la importación.')

# 21. Creación del apartado Socios comerciales de Streamlit
def socios(comercio2021, productoPaisExp, productoPaisImp):

    st.title('Los socios comerciales de Países Bajos')
    st.subheader('Implicaciones del comercio internacional')
    st.markdown('Un saldo comercial positivo refleja una economía fuerte y competitiva capaz de producir productos y servicios que son \
        demandados en el mercado internacional. Esto contribuye al crecimiento económico del país, ya que las exportaciones generan ingresos \
        y empleo, e impulsa la inversión y la innovación.')
    st.markdown('Por otra parte, un saldo comercial negativo indica una dependencia sobre ciertos bienes y servicios que un país no está \
        produciendo internamente, lo que puede tener implicaciones para la seguridad económica y la autonomía. La importación de una gran \
        cantidad de bienes de otros países podría competir con la producción local, lo que podría tener implicaciones para la industria nacional \
        y potencialmente llevar a la pérdida de empleos en ciertos sectores.')
    st.markdown('En el apartado anterior hemos visto como las exportaciones e importaciones neerlandesas se concentran en Europa, Estados Unidos \
        y China. Analizando los diez países a los que más se exporta y los diez países de los que más se importa se pueden identificar similitudes \
        y diferencias. Ciertos países, al menos en su relación con Países Bajos, tendrán un papel de proveedor, y otros, un papel de comprador.')
    st.markdown('Desglosando estos números, podemos observar que, entre los principales socios comerciales, los siguientes países son \
        compradores: Alemania (saldo comercial de +24.689 millones de €), Francia (+23.748), Reino Unido (+14.446), Italia (+8.723), España \
        (+7.772), Bélgica (7.313), Polonia (+7.293) y Suecia (+3.779).')
    st.markdown('Todos los países mencionados pertenecen a la Unión Europea, salvo Reino Unido tras el Brexit, cuyas relaciones comerciales \
        históricas con Países Bajos también pueden ser encuadradas en el mismo contexto que las del resto de países. Además de la exportación de \
        bienes de producción propia, también hay que considerar en este cálculo otros conceptos, y es que Países Bajos funciona también como \
        intermediario en el comercio internacional, reexportando bienes al resto de países del continente europeo.')
    st.markdown('Por otro lado, China (saldo comercial de -39.801 millones de €), Estados Unidos (-12.441) y Rusia (-6.899) son países \
        proveedores.')
    st.markdown('Entre sus socios comerciales más importantes, solo tres mantienen un saldo comercial positivo con Países Bajos, siendo además \
        estos las tres principales potencias mundiales. Existe un serio peligro en tener una dependencia externa de recursos clave como lo \
        pueden ser la tecnología o la energía. El producto más importado desde China en 2021 fue “Equipamiento de telecomunicaciones”. El \
        producto más importado desde Estados Unidos y Rusia en 2021 fue “Aceites petrolíferos y otros”. La reciente guerra de Ucrania ha tenido \
        consecuencias fatales para Países Bajos y resto de países europeos y dejado en evidencia la necesidad de ser autosuficientes en estos \
        campos. Aunque en menor medida, la crisis de los microchips también tuvo un impacto en el posicionamiento comercial de países europeos \
        respecto a bienes estratégicos.')

    opcion = st.radio(label='Visualizar:', options=('Exportaciones', 'Importaciones'))

    if opcion == 'Exportaciones':
        
        st.write('Exportaciones de bienes (en millones de €) desde Países Bajos en 2021 (top 10 países)')
        mapexp = mapaInteractivoExp(comercio2021)
        folium_static(mapexp, width=725)
        with st.expander('Descripción'):
            st.write('En este mapa se pueden apreciar enumerados los 10 principales países de destino en las exportaciones de bienes \
                     desde Países Bajos en 2021. Al hacer click sobre el marcador de cada país se puede apreciar el valor de la \
                     exportación (en millones de €)')
            
        st.write('Cuota de las exportaciones generadas por los primeros 32 países en 2021')
        treemapexp = treemapExp(comercio2021)
        st.pyplot(treemapexp)
        with st.expander('Descripción'):
            st.write('Treemap o mapa de árbol que refleja la cuota de cada país sobre el total de las exportaciones de bienes a Países Bajos \
                generadas por los primeros 32 países en 2021')
        
        st.write('Producto más exportado a cada país')
        st.dataframe(productoPaisExp)
        with st.expander('Descripción'):
            st.write('Tabla que recoge el producto (SITC Nivel 3) que más se exportó desde Países Bajos en 2021 a cada país de entre los diez países a los que \
                más se exportó')

    if opcion == 'Importaciones':
        
        st.write('Importaciones de bienes (en millones de €) a Países Bajos en 2021 (top 10 países)')
        mapimp = mapaInteractivoImp(comercio2021)
        folium_static(mapimp, width=725)
        with st.expander('Descripción'):
            st.write('En este mapa se pueden apreciar enumerados los 10 principales países de origen en las importaciones de bienes a Países \
                Bajos en 2021. Al hacer click sobre el marcador de cada país se puede apreciar el valor de la importación (en millones de €)')
            
        st.write('Cuota de las importaciones generadas por los primeros 32 países en 2021')
        treemapimp = treemapImp(comercio2021)
        st.pyplot(treemapimp)
        with st.expander('Descripción'):
            st.write('Treemap o mapa de árbol que refleja la cuota de cada país sobre el total de las importaciones de bienes a Países Bajos \
                generadas por los primeros 32 países en 2021')
        
        st.write('Producto más importado desde cada país')
        st.dataframe(productoPaisImp)
        with st.expander('Descripción'):
            st.write('Tabla que recoge el producto (SITC Nivel 3) que más se importó a Países Bajos en 2021 desde cada país de entre los diez países desde los \
                que más se importó')

# 22. Creación del apartado Productos comercializados de Streamlit
def productos(comercio2021, sitc):

    st.title('Productos por categorías')
    st.subheader('Clasificación SITC')
    st.write('La Standard International Trade Classification (SITC) clasifica bienes exportados e importados por un país de forma estandarizada \
        para permitir la comparación entre países y periodos. Se recomienda utilizar la clasificación SITC únicamente con propósito analítico \
        (se recomienda recoger las estadísticas comerciales mediante la clasificación Harmonized System, HS). En este trabajo todos los productos \
        han sido analizados mediante su código SITC, ya que la base de datos de la CBS así los clasifica.')
    st.write('Existen diez categorías SITC principales (nos referiremos a estas categorías como SITC de nivel 1) enumeradas del 0 al 9. Estas \
        categorías se conforman por subcategorías (SITC de nivel 2) que a su vez están conformadas por subcategorías (SITC de nivel 3). De esta \
        manera, cuanto más bajo sea el nivel del SITC, más precisa será la definición de su categoría. A modo de ejemplo: 0 - Food And Live \
        Animals; 05 - Vegetables And Fruit; 057 - Fruit And Nuts, Fresh Or Dried.')
    st.image('images/tulips_molen.jpg', caption='Países Bajos es el mayor exportador de flores del mundo')
    st.subheader('Productos comercializados por Países Bajos')
    st.write('Los productos más exportados en Países Bajos son un reflejo de sectores donde la producción local es competitiva o donde el país \
        es un agente intermediario con un buen posicionamiento. Por otro lado, las importaciones permiten a Países Bajos adquirir bienes cuando \
        su producción local no satisface las necesidades o demanda del país.')
    st.write('Atendiendo al SITC de nivel 1, los productos más exportados son “Maquinaria y material de transporte” (165.532  millones de €), \
        “Sustancias químicas y productos relacionados” (106.886) y “Artículos manufacturados diversos” (70.641). Los productos más importados \
        coinciden, y en el mismo orden, con importaciones con valor de 160.067, 75.074 y 72.071 millones de € respectivamente.')
    st.write('Atendiendo al SITC de nivel 2, los productos más exportados son “Máquinas y aparatos eléctricos” (36.410  millones de €), \
        “Productos medicinales y farmacéuticos” (31.570) y “Maquinaria para industrias particulares” (29.765). Los productos más importados \
        son “Petróleo y relacionados” (52.189 millones de €), “Máquinas y aparatos eléctricos” (40.459) y “Aparatos de telecomunicaciones y \
        otros” (27.608).')
    st.write('Atendiendo al SITC de nivel 3, los productos más exportados son “Productos petrolíferos, refinado” (26.943 millones de €), \
        “Equipamiento de telecomunicaciones” (20.889) y “Otra maquinaria especializada” (20.185). Los productos más importados son “Petróleo, \
        crudo” (29.893 millones de €), “Equipamiento de telecomunicaciones” (23.100) y “Productos petrolíferos, refinado” (22.296).')
    st.write('Podemos observar que los productos con los que Países Bajos comercia más son de alto valor, ya sean petróleo, maquinaria \
        industrial, químicos, productos farmacéuticos o aparatos eléctricos. Algunos bienes serán consumidos en el país. Otros productos \
        importados serán transformados y exportados de nuevo. Otros productos serán simplemente distribuidos a países terceros.')
    st.write('Categorías como “Bebidas y tabaco”, “Materiales, excepto combustible” y “Aceites animales y vegetales” tienen una relevancia \
        menor en el comercio exterior neerlandés. Cabe destacar la categoría “Alimentos y animales”, la cual se coloca como cuarto producto \
        más exportado (sexto más importado) en Países Bajos. Las industrias de la agricultura y cárnica están muy desarrolladas en el país, e \
        incorporan tecnologías que potencian su competitividad.')
    rasgos = st.radio(label='Visualizar:', options=('Exportaciones', 'Importaciones'))

    if rasgos == 'Exportaciones':
        
        st.write('Productos (SITC Nivel 1) más exportados (en millones de €) desde Países Bajos en 2021')
        lollipopexp1 = lollipopExp1(comercio2021, sitc)
        st.pyplot(lollipopexp1)
        with st.expander('Descripción'):
            st.write('Este gráfico muestra las diez categorías de producto (SITC Nivel 1) que existen y sus exportaciones en millones de € \
                desde Países Bajos en 2021')

        st.write('Productos (SITC Nivel 2) más exportados (en millones de €) desde Países Bajos en 2021')    
        lollipopexp2 = lollipopExp2(comercio2021, sitc)
        st.pyplot(lollipopexp2)
        with st.expander('Descripción'):
            st.write('Este gráfico muestra las diez categorías de producto (SITC Nivel 2) que más se exportaron desde Países Bajos en 2021 \
                y sus valores en millones de €')

        st.write('Productos (SITC Nivel 3) más exportados (en millones de €) desde Países Bajos en 2021')    
        lollipopexp3 = lollipopExp3(comercio2021, sitc)
        st.pyplot(lollipopexp3)
        with st.expander('Descripción'):
            st.write('Este gráfico muestra las diez categorías de producto (SITC Nivel 3) que más se exportaron desde Países Bajos en 2021 \
                y sus valores en millones de €')
            
    if rasgos == 'Importaciones':
        
        st.write('Productos (SITC Nivel 1) más importados (en millones de €) desde Países Bajos en 2021')
        lollipopimp1 = lollipopImp1(comercio2021, sitc)
        st.pyplot(lollipopimp1)
        with st.expander('Descripción'):
            st.write('Este gráfico muestra las nueve categorías de producto (SITC Nivel 1) que existen y sus importaciones en millones de € \
                desde Países Bajos en 2021')

        st.write('Productos (SITC Nivel 2) más importados (en millones de €) desde Países Bajos en 2021')    
        lollipopimp2 = lollipopImp2(comercio2021, sitc)
        st.pyplot(lollipopimp2)
        with st.expander('Descripción'):
            st.write('Este gráfico muestra las diez categorías de producto (SITC Nivel 2) que más se importaron a Países Bajos en 2021 \
                y sus valores en millones de €')
            
        st.write('Productos (SITC Nivel 3) más importados (en millones de €) desde Países Bajos en 2021')    
        lollipopimp3 = lollipopImp3(comercio2021, sitc)
        st.pyplot(lollipopimp3)
        with st.expander('Descripción'):
            st.write('Este gráfico muestra las diez categorías de producto (SITC Nivel 3) que más se importaron a Países Bajos en 2021 \
                y sus valores en millones de €')
            
# 23. Creación del apartado Tendencias en el comercio exterior de Streamlit
def tendencias(comercio):
    st.title('Una tendencia clara')
    st.subheader('El comercio exterior neerlandés en los últimos diez años')
    st.write('La tendencia en el comercio exterior neerlandés refleja una continua expansión y diversificación de sus relaciones comerciales. \
        A pesar de existir una alta similitud entre las variaciones de las exportaciones e importaciones, existen pequeñas diferencias.')
    st.write('Las exportaciones se mantuvieron en unos niveles estables en el periodo 2012-2016. Tras este periodo, el crecimiento anual ha \
        sido considerable, únicamente opacado en el año 2020 por la pandemia y sus claras consecuencias en el comercio internacional. Además, \
        las exportaciones en 2021 se recuperaron de tal forma que superaron cualquier nivel previamente alcanzado. Las variaciones de las \
        exportaciones por países también son similares en todos los casos. Cabe destacar que las variaciones anuales en las exportaciones a \
        Alemania, pese a seguir las tendencias del resto de países, sí se dan de forma más pronunciada.')
    st.write('En cuanto a las importaciones, estas se redujeron anualmente de forma moderada en el periodo 2012-2016. No fue hasta a partir de \
        entonces cuando las importaciones empezaron a crecer, y además a un ritmo elevado. Al igual que con las exportaciones, las importaciones \
        también acusaron la crisis de la Covid-19. En 2021, tras volver a la normalidad, también se batió el nivel máximo previo.')
    st.write('Pese a que CBS no ofrece datos completos para el año 2022 (a día 30 de octubre de 2023), existen otras fuentes, como Trademap.org, \
        que sí los ofrecen. Los valores absolutos no pueden compararse entre ambas fuentes, pues la metodología de obtención de datos ha sido \
        diferente, pero sí se pueden analizar las tendencias. En 2022, el crecimiento de tanto las exportaciones (+10,54 %), como las \
        importaciones (+14,35 %), ha vuelto a ser muy elevado.')
    st.write('La expectativa para los próximos años es de crecimiento continuado en ambos apartados. Existen ciertos peligros o riesgos para \
        el comercio exterior mundial, como políticas proteccionistas, debilitaciones en las relaciones comerciales entre países o guerras. \
        Pese a cierta incertidumbre y posibles contratiempos, la tendencia actual no debería variar, por lo menos, en el corto/medio \
        plazo.')
    prioridad = st.radio(label='Visualizar:', options=('Exportaciones', 'Importaciones'))
    if prioridad == 'Exportaciones':
        
        st.write('Exportaciones neerlandesas en los últimos diez años')
        barplotexp = barplotExp(comercio)
        st.image(barplotexp)
        with st.expander('Descripción'):
            st.write('Gráfico que muestra las exportaciones totales desde Países Bajos en millones de € para cada uno de los últimos diez años \
                (2012-2021)')

        st.write('Exportaciones neerlandesas en los últimos diez años por país (top 10 países)')
        timeseriesexp = timeseriesExp(comercio)
        st.image(timeseriesexp, width=800)
        with st.expander('Descripción'):
            st.write('Gráfico que muestra las exportaciones totales desde Países Bajos en millones de € para cada uno de los últimos diez años \
                (2012-2021) por país (top 10 países a los que más se exporta)')

    if prioridad == 'Importaciones':

        st.write('Importaciones neerlandesas en los últimos diez años') 
        barplotimp = barplotImp(comercio)
        st.image(barplotimp)
        with st.expander('Descripción'):
            st.write('Gráfico que muestra las importaciones totales a Países Bajos en millones de € para cada uno de los últimos diez años \
                (2012-2021)')

        st.write('Importaciones neerlandesas en los últimos diez años por país (top 10 países)')
        timeseriesimp = timeseriesImp(comercio)
        st.image(timeseriesimp, width=800)
        with st.expander('Descripción'):
            st.write('Gráfico que muestra las importaciones totales a Países Bajos en millones de € para cada uno de los últimos diez años \
                (2012-2021) por país (top 10 países desde los que más se importa)')

# 24. Creación del apartado Conclusión de Streamlit
def conclusion():
    st.title('Conclusión')
    st.write('Países Bajos es uno de los agentes comerciales más relevantes a nivel mundial. Los datos de exportaciones e importaciones así lo \
        reflejan. Su fortaleza en el continente europeo es indiscutible. Además de comercializar en volúmenes muy elevados, los productos son \
        de un alto valor.')
    st.write('Su posición geográfica estratégica, su avanzada infraestructura y logística, y el puerto de Róterdam son algunos de los factores \
        que favorecen el comercio exterior con el resto de países europeos. Además, obtiene gran parte de aquellos recursos o bienes que no es \
        capaz de producir desde China, Estados Unidos y Rusia, principales potencias políticas mundiales.')
    st.image('images/dutch_parlament.jpg', caption='El parlamento neerlandés se encuentra en la ciudad de La Haya')
    st.write('Países Bajos tiene una dependencia energética exterior. El producto principal que importa desde Rusia y Estados Unidos es \
        “Aceites petrolíferos y otros”. Los productos que exporta son variados, pero provenientes todos de sectores tecnológicos. Además de \
        “Productos petrolíferos, refinado”, los productos que más exporta están relacionados con la maquinaria industrial, equipos de \
        telecomunicaciones y medicamentos.')
    st.write('Tanto las exportaciones como las importaciones han experimentado aumentos anuales elevados en los últimos cinco años. Únicamente \
        la pandemia ralentizó en 2020 las cifras del comercio exterior. Se espera una continuidad en los aumentos de exportaciones e \
        importaciones en el futuro cercano que permitirán a Países Bajos mantenerse como una de las referencias mundiales en el comercio \
        exterior.')
    st.markdown('*Análisis elaborado por Jon Pinies Echeguren*') 
    st.write('LinkedIn: https://www.linkedin.com/in/jon-pinies-echeguren/')
    st.write('Github: https://github.com/JonPiniesEcheguren')