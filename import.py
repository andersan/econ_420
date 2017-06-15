import pandas as pd
import numpy as np
from os import chdir
import glob
import test


chdir("/home/cree/Downloads/br_econ/")
count = 0
mun, state = {}, {}

mun = import_data("mun")
state = import_data("state")

# municipal dataframes
df = mun.get('mun/Renda_municipios - Renda familiar - per capita - media.csv')
df1 = mun.get('mun/mun_media_anos_de_estudos_25_anos_+_todos.csv')
df2 = mun.get('mun/mun_Mortalidade infantil (por mil nascidos vivos)_1970-2000.csv') 
df3	= mun.get('mun/populacao_municipal.csv')

#state dataframes
df4 = state.get('state/estado_Renda domiciliar per capita - media_1976 - 2014.csv')
df5 = state.get('state/Anos de estudo - media - pessoas 25 anos e mais - 1981 - 2014.csv')
df6 = state.get('state/Anos de estudo - media - pessoas 25 anos e mais - mulheres 1981 -2014.csv')
df7 = state.get('state/populcao_estado_1980-2014.csv')
df8 = state.get('state/populacao_residente_estado_1970-2000.csv')

#calcular mortalidade infantil por estado
df9 = df8[['Sigla', 'Código', 'Estado']].copy()
df10 = df2.drop('Código', 1).groupby('Sigla').mean()
df10.reset_index(level='Sigla', inplace=True)
df9 = pd.merge(df9,df10, on='Sigla')