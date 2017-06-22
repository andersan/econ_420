import pandas as pd
import numpy as np
from os import chdir
import functions

chdir("/home/cree/Downloads/br_econ/MHDI/")

count = 0
mun, state = {}, {}


# columns to name vars from CSV files
columns = ["locale","locale_type","codigo","life_ex_1991","life_ex_2000",\
           "life_ex_2010","inf_mortality_1991","inf_mortality_2000",\
           "inf_mortality_2010","MHDI_1991","MHDI_2000","MHDI_2010",\
           "MHDI_income_1991","MHDI_income_2000","MHDI_income_2010",\
           "MHDI_life_ex_1991","MHDI_life_ex_2000","MHDI_life_ex_2010",\
           "MHDI_education_1991","MHDI_education_2000","MHDI_education_2010",\
           "education_1991","education_2000","education_2010","income_1991",\
           "income_2000","income_2010"]

columns_small = ["locale","locale_type","codigo","life_ex_2000","life_ex_2010",\
                 "inf_mortality_2000","inf_mortality_2010","MHDI_2000","MHDI_2010",\
                 "MHDI_income_2000","MHDI_income_2010","MHDI_life_ex_2000",\
                 "MHDI_life_ex_2010","MHDI_education_2000","MHDI_education_2010",\
                 "education_2000","education_2010","income_2000","income_2010"]

# use data from 1991, 2000, 2010
cities  = functions.import_data("data_cities.csv", columns, 5567)
states = functions.import_data("data_states.csv", columns, 29)

# use data from 2000, 2010
MAs     = functions.import_data("data_metro_areas.csv", columns_small, 22)
regions = functions.import_data("data_regional_divisions.csv", columns_small, 187) 


chdir("/home/cree/workspace/econometrics/")