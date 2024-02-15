import streamlit as st
import numpy as np
import json 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from io import BytesIO
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from utils import DIC_COLORES, convert_df, get_dic_colors, get_dic_colors_area


st.title('Herramienta interna PGN')


st.subheader('Desagregados 2023')

tdd = pd.read_csv('test_desagregados_2023.csv')
tdd[['cuenta', 'subcuenta', 'proyecto', 'subproyecto']] = tdd[['cuenta', 'subcuenta', 'proyecto', 'subproyecto']].fillna('') 
fig = px.sunburst(tdd, path=[px.Constant('PGN'), 
                                 'sector', 
                                 'entidad', 
                                 'cuenta_g', 'cuenta', 'subcuenta'], 
                                  values='total_def_2024',
                      color='sector_code')
st.plotly_chart(fig)

csv = convert_df(tdd)

st.download_button(
                label="Descargar datos desagregados - 2023",
                data=csv,
                file_name='datos_desagregados_2024.csv',
                mime='text/csv')


st.subheader('Desagregados 2024')
tdd = pd.read_csv('test_desagregados_datos.csv')
tdd[['cuenta', 'subcuenta', 'proyecto', 'subproyecto']] = tdd[['cuenta', 'subcuenta', 'proyecto', 'subproyecto']].fillna('') 
fig = px.sunburst(tdd, path=[px.Constant('PGN'), 
                                 'sector', 
                                 'entidad', 
                                 'cuenta_g', 'cuenta', 'subcuenta'], 
                                  values='total',
                      color='sector_code')
st.plotly_chart(fig)

csv = convert_df(tdd)

st.download_button(
                label="Descargar datos desagregados - 2024",
                data=csv,
                file_name='datos_desagregados_2024.csv',
                mime='text/csv')

