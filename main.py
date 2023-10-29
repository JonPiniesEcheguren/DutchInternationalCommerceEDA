import streamlit as st
import functions as fu
import variables as va

# STREAMLIT - VISUALIZACIÓN DE DATOS
# 1. Creamos la configuración de la página, y el título
st.set_page_config(page_title='Comercio exterior en Países Bajos', layout='wide', page_icon='chart_with_upwards_trend')

# 2. Creamos el menú con los distintos apartados dentro de la página
menu = st.sidebar.selectbox(label='Seleccione una opción:', options=('Inicio', 'Visión general', 'Socios comerciales', 'Productos comercializados', 'Tendencias en el comercio exterior', 'Conclusión'))
if menu == 'Inicio':
    fu.inicio()
if menu == 'Visión general':
    fu.visionGeneral(va.globo2021)
if menu == 'Socios comerciales':
    fu.socios(va.comercio2021, va.productoPaisExp, va.productoPaisImp)
if menu == 'Productos comercializados':
    fu.productos(va.comercio2021, va.sitc)
if menu == 'Tendencias en el comercio exterior':
    fu.tendencias(va.comercio)
if menu == 'Conclusión':
    fu.conclusion()
