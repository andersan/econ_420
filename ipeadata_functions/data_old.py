import pandas as pd
import numpy as np
from os import chdir
import functions

#improvements: change variable names to be more intuitive

chdir("/home/cree/Downloads/br_econ/")

count = 0
mun, state = {}, {}

mun = functions.import_data("mun")
state = functions.import_data("state")

chdir("/home/cree/workspace/econometrics/")

# municipal dataframes
mun_renda = functions.data_prep(mun.get('mun/Renda_municipios - Renda familiar - per capita - media.csv'))
mun_ensino = functions.data_prep(mun.get('mun/mun_media_anos_de_estudos_25_anos_+_todos.csv'))
mun_saude = mun.get('mun/mun_Mortalidade infantil (por mil nascidos vivos)_1970-2000.csv')
mun_populacao_censo  = functions.data_prep(mun.get('mun/populacao_municipal.csv'))
mun_renda_2, mun_ensino_2 = mun_renda.ix[3:].copy(),mun_ensino.ix[3:].copy()
mun_renda, mun_ensino = mun_renda.ix[:3],mun_ensino.ix[:3]

#state dataframes
state_renda = functions.data_prep(state.get('state/estado_Renda domiciliar per capita - media_1976 - 2014.csv'))
state_ensino = functions.data_prep(state.get('state/Anos de estudo - media - pessoas 25 anos e mais - 1981 - 2014.csv'))
state_ensino_mulheres = functions.data_prep(state.get('state/Anos de estudo - media - pessoas 25 anos e mais - mulheres 1981 -2014.csv'))
state_populacao_anual = functions.data_prep(state.get('state/populcao_estado_1980-2014.csv'))
state_populacao_censo = state.get('state/populacao_residente_estado_1970-2000.csv')

#calcular mortalidade infantil por estado
df9 = state_populacao_censo[['Sigla', 'Código', 'Estado']].copy()
df10 = mun_saude.drop('Código', 1).groupby('Sigla').mean()
df10.reset_index(level='Sigla', inplace=True)

state_saude = functions.data_prep(pd.merge(df9,df10, on='Sigla'))
state_populacao_censo = functions.data_prep(state.get('state/populacao_residente_estado_1970-2000.csv'))
mun_saude = functions.data_prep(mun.get('mun/mun_Mortalidade infantil (por mil nascidos vivos)_1970-2000.csv'))

# data_vars = [state_saude, state_populacao_censo,state_populacao_anual,\
#              state_ensino_mulheres,state_ensino,state_renda,          \
#              mun_populacao_censo,mun_saude,mun_ensino,\
#              mun_renda]
