import functions
import data
import pandas as pd
import numpy as np
import statsmodels.api as sm

def OLS(df1,df2,state):
  df1,df2 = functions.compare_years(functions.numpy_to_pd(df1),functions.numpy_to_pd(df2))
  df2 = sm.add_constant(df2)
  print(df1[state],df2[state])
  df1Xdf2 = sm.OLS(df1[state], df2[state], missing='drop').fit()
  # print(df1Xdf2.summary())
  return df1Xdf2;

for state in data.state_renda:
  if state != 'Year':
    OLS(data.state_ensino, data.state_populacao_anual, state)

# renda, ensino = functions.compare_years(data.state_renda, data.state_ensino)
# ensino = sm.add_constant(ensino)
# State_rendaXensino = sm.OLS(ensino['Santa Catarina'], renda['Santa Catarina'], missing='drop').fit()
# print(State_rendaXensino.summary())
# renda, ensino = functions.compare_years(data.municipio_renda, data.state_ensino)
# ensino = sm.add_constant(ensino)
# City_rendaXensino = sm.OLS(ensino['Santa Catarina'], renda['Santa Catarina'], missing='drop').fit()
# print(State_rendaXensino.summary())
# print(sm.OLS(ensino['1993'], renda['1993'], missing='drop'))
# print(results.f_test(np.identity(2)))
# for row in renda.itertuples():
#   rendaXensino = sm.OLS(ensino.loc[row[0]], renda.loc['Santa Catarina'], missing='drop').fit()
#   print(rendaXensino.summary())
## cant compare 2 large tables like this... need to grab cities and states ONE BY ONE and compare them?


# #OLS functions
# functions.OLS(data.municipio_renda,data.municipio_ensino)
# functions.OLS(data.municipio_ensino,data.municipio_saude)
# functions.OLS(data.municipio_saude,data.municipio_renda)
# functions.OLS(data.state_renda,data.state_ensino)
# functions.OLS(data.state_saude,data.state_ensino)
# functions.OLS(data.state_renda,data.state_saude)