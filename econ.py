import functions
import pandas as pd
import numpy as np
import statsmodels.api as sm
from os import chdir
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from matplotlib import pyplot
from statsmodels.graphics.regressionplots import abline_plot
import patsy

chdir("/home/cree/Downloads/br_econ/MHDI/")

### NOTE: inf_mortality and life_ex cause multicollinearity in OLS regressions
# income = dependent var
income_formula     = 'income ~ education + life_ex + inf_mortality'
# health = dependent var
health_formula     = 'life_ex ~ education + income ' # can substitute inf_mortality for life_ex
# education = dependent var
education_formula  = 'education ~ income + life_ex + inf_mortality'

# same models, using MHDI variables:
# income = dependent var
MHDI_income_formula = 'MHDI_income ~ MHDI_education + MHDI_life_ex'
# health = dependent var
MHDI_health_formula = 'MHDI_life_ex ~ MHDI_education + MHDI_income'
# education = dependent var
MHDI_education_formula = 'MHDI_education ~ MHDI_income + MHDI_life_ex'

formulas = [income_formula,
            health_formula,
            education_formula,
            MHDI_income_formula,
            MHDI_health_formula,
            MHDI_education_formula]

formulas_locale = [s + ' + C(locale)' for s in formulas]

formulas_year = [s + ' + C(year)' for s in formulas]

formulas_both =[s + ' + C(year) + C(locale)' for s in formulas]
            
all_formulas = [formulas, formulas_locale, formulas_year, formulas_both]

# TODO: would like to learn how to include years as a variable, with education as lagging behind income
#                      and health, or health lagging behind income

# variables that can be compared:
#             inf_mortality (infant mortality)
#             life_ex (life expectancy)
#             locale
#             locale_type
#             year
#             education (expected number of years of schooling for people entering 1st year of school)
#             income (per capita GNI)
#     MDHI variables run on a scale of 0 to 1
#             MHDI (human development index)
#             MHDI_income (PER CAPITA GNI)
#             MHDI_life_ex (LIFE EXPECTANCY)
#             MHDI_education (MEAN YEARS SCHOOLING 25+ and EXPECTED YEARS SCHOOLING, averaged together)

cities  = pd.read_csv("formatted_data_cities.csv")
states = pd.read_csv("formatted_data_states.csv")
MAs     = pd.read_csv("formatted_data_metro_areas.csv")
regions = pd.read_csv("formatted_data_regional_divisions.csv")
HDUs = pd.read_csv("formatted_data_human_development_units.csv")

# GRAPH SIMPLE OLS REGRESSIONS OF ALL MHDI FACTORS (1x1, not multiple variable regressions)

functions.sns_graph(states,'Income vs Health','MHDI_life_ex','Health','MHDI_income','Income')
functions.sns_graph(states,'Income vs Education','MHDI_education','Education','MHDI_income','Income')
functions.sns_graph(states,'Education vs Income','MHDI_income','Income','MHDI_education','Education')
functions.sns_graph(states,'Education vs Health','MHDI_life_ex','Health','MHDI_education','Education')
functions.sns_graph(states,'Health vs Education','MHDI_education','Education','MHDI_life_ex','Health')
functions.sns_graph(states,'Health vs Income','MHDI_income','Income','MHDI_life_ex','Health')


# return r squared values for all patsy formluas passed into it... must be a list of formulas
  
# for f in all_formulas:
  # print(functions.rsquared(MAs, f))
  # print(functions.rsquared(regions, f))
  # print(functions.rsquared(HDUs, f))
  # print(functions.rsquared(cities, f))

from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor

# PRINT VARIABLE INFLATION FACTOR, SPLIT FUNCTION INTO X AND Y
# Break into left and right hand side; y and X
y, X = dmatrices(formulas_year[1], data=regions, return_type="dataframe")

# For each Xi, calculate VIF
vif = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# Fit X to y
result = sm.OLS(y, X).fit()
print(formulas_year[5], 'VIF: ', vif)

# PRINT ALL PARAMETERS FROM OLS

ols = smf.ols(income_formula, data=regions).fit()
print('Summary: ', ols.summary())
print('Covariance: ', ols.cov_params())
print('Parameters: ', ols.params)
print('Standard errors: ', ols.bse)
print('Predicted values: ', ols.predict())
print('R2: ', ols.rsquared)


# StatsModels OLS - not used
# basic_ols = sm.OLS(regions['education'],regions[['income','life_ex', 'inf_mortality']],missing='drop').fit()
# print(basic_ols.summary())