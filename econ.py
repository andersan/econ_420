import functions
# import data
import pandas as pd
import numpy as np
import statsmodels.api as sm
from os import chdir

chdir("/home/cree/Downloads/br_econ/MHDI/")

# input any two variables and output OLS regressions for all states
# (parameters: two state level dataframes from data.py)
def OLS(df1,df2,df3 = pd.DataFrame({'A' : []})):
    # 2 arguments (simple regression)
  if df3.empty:
    df1,df2 = functions.compare_years(functions.numpy_to_pd(df1), \
                functions.numpy_to_pd(df2))
    df2 = sm.add_constant(df2, has_constant='add')
    results = []
    for col in df1:
      if col != 'Year':
        # print(df1[state],df2[state])
        one = df1[col]
        two = df2[[col,'const']]
        est = sm.OLS(one, two, missing='drop').fit()
        # print(est.summary())
        # sm(est)
        results.append(est)
  # 3 arguments (multiple regression)
  else: 
    df1,df2,df3 = functions.compare_years(functions.numpy_to_pd(df1), \
                functions.numpy_to_pd(df2),functions.numpy_to_pd(df3))
    df2 = sm.add_constant(df2, has_constant='add')
    # print(df1,df2,df3)
    results = []
    for col in df1:
      if col != 'Year':
        # print(df1[state],df2[state])
        one = df1[col]
        two = df2[[col,'const']].join(df3[col], rsuffix='**2**')
        print(one,two)
        est = sm.OLS(one, two, missing='drop').fit()
        # print(est.summary())
        # sm.SummarizeResults(est)
        results.append(est)
  return results;

# 
#  TODO:
# 
#  - fixed effects model (with error and dummy var/constant)
#       - implement dummy vars
#       - figure out how to use pansy formulas
#       - use latex to print models for paper
# 
#  - R2, std deviations
#       - choose which statistics to measure 
#           - what locations to run regressions on??? what indicators???
# 
#  - scatterplots
#       - build a fit graph for ed, income and health functions 
#
#  - OLS/FE: run regressions
# 
#  - final stretch:
#       - export data/graphs for paper
#       - explain data and turn in paper




# variables that can be compared:
#             inf-mortality
#             life-ex
#             locale
#             locale_type
#             year
#             MHDI
#             MHDI-income
#             MHDI-life-ex
#             MHDI-education
#             education
#             income
# 
# examples
# linear OLS uses:
# basic_ols = sm.OLS(regions['education'],regions[['income','life-ex', 'inf-mortality']],missing='drop').fit()
# print(basic_ols.summary())


# cities  = pd.read_csv("formatted_data_cities.csv")
# states = pd.read_csv("formatted_data_states.csv")
# MAs     = pd.read_csv("formatted_data_metro_areas.csv")
regions = pd.read_csv("formatted_data_regional_divisions.csv") 
print(regions['education'])
# basic_ols = sm.OLS(regions['education'],regions[['income','life-ex', 'inf-mortality']],missing='drop').fit()
# print(basic_ols.summary())

# print(OLS(data.state_ensino, data.state_populacao_anual))
# print(OLS(data.mun_ensino,data.mun_renda, data.mun_saude))



# renda, ensino = functions.compare_years(data.state_renda, data.state_ensino)
# ensino = sm.add_constant(ensino)
# State_rendaXensino = sm.OLS(ensino['Santa Catarina'], renda['Santa Catarina'], missing='drop').fit()
# print(State_rendaXensino.summary())
# renda, ensino = functions.compare_years(data.mun_renda, data.state_ensino)
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
# functions.OLS(data.mun_renda,data.mun_ensino)
# functions.OLS(data.mun_ensino,data.mun_saude)
# functions.OLS(data.mun_saude,data.mun_renda)
# functions.OLS(data.state_renda,data.state_ensino)
# functions.OLS(data.state_saude,data.state_ensino)
# functions.OLS(data.state_renda,data.state_saude)