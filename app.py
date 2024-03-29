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





