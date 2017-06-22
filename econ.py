import functions
# import data
import pandas as pd
import numpy as np
import statsmodels.api as sm
from os import chdir
import statsmodels.formula.api as smf

chdir("/home/cree/Downloads/br_econ/MHDI/")

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

# attempt at using pansy formulas...
# 
# income = dependent var 
income_formula     = 'income ~ education + (life_ex + np.log(inf_mortality)) + C(year)'
# health = dependent var 
health_formula     = '(life_ex + np.log(inf_mortality)) ~ education + income + C(year)'
# education = dependent var 
education_formula  = 'education ~ income + (life_ex + np.log(inf_mortality)) + C(year)'

# same models, using MHDI variables:
# 
# income = dependent var 
MHDI_income_formula = 'MHDI_income ~ MHDI_education + MHDI_life_ex + C(year)'
# health = dependent var 
MHDI_health_formula = 'MHDI_life_ex ~ MHDI_education + MHDI_income + C(year)'
# education = dependent var 
MHDI_education_formula = 'MHDI_education ~ MHDI_income + MHDI_life_ex + C(year)'

# TODO: would like to learn how to include years as a variable, with education as lagging behind income
#                      and health, or health lagging behind income

# variables that can be compared:
#             inf_mortality
#             life_ex
#             locale
#             locale_type
#             year
#             MHDI
#             MHDI_income (PER CAPITA GNI)
#             MHDI_life_ex (HEALTH)
#             MHDI_education (MEAN YEARS SCHOOLING 18+ + EXPECTED YEARS SCHOOLING)
#             education
#             income
# 
# examples
# linear OLS uses:
# basic_ols = sm.OLS(regions['education'],regions[['income','life_ex', 'inf_mortality']],missing='drop').fit()
# print(basic_ols.summary())
# 
# formula OLS uses:
# formula_ols = smf.ols('MHDI_income ~ MHDI_education + MHDI_life_ex + C(locale)', data=MAs).fit()
# print(formula_ols.summary())

# cities  = pd.read_csv("formatted_data_cities.csv")
# states = pd.read_csv("formatted_data_states.csv")
MAs     = pd.read_csv("formatted_data_metro_areas.csv")
# regions = pd.read_csv("formatted_data_regional_divisions.csv") 
# print(regions['education'])
# basic_ols = sm.OLS(regions['education'],regions[['income','life_ex', 'inf_mortality']],missing='drop').fit()
# print(basic_ols.summary())

formula_ols = smf.ols(MHDI_health_formula, data=MAs).fit()
print(formula_ols.summary())
print(MAs.loc[MAs['locale'] == 'RM Recife'])
print(MAs)