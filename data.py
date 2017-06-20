import pandas as pd
import numpy as np
from os import chdir
import functions

chdir("/home/cree/Downloads/br_econ/MHDI/")

count = 0
mun, state = {}, {}


# columns to name vars from CSV files
columns = ["locale","locale_type","codigo","life-ex-1991","life-ex-2000",\
           "life-ex-2010","inf-mortality-1991","inf-mortality-2000",\
           "inf-mortality-2010","MHDI-1991","MHDI-2000","MHDI-2010",\
           "MHDI-income-1991","MHDI-income-2000","MHDI-income-2010",\
           "MHDI-life-ex-1991","MHDI-life-ex-2000","MHDI-life-ex-2010",\
           "MHDI-education-1991","MHDI-education-2000","MHDI-education-2010",\
           "education-1991","education-2000","education-2010","income-1991",\
           "income-2000","income-2010"]

columns_small = ["locale","locale_type","codigo","life-ex-2000","life-ex-2010",\
                 "inf-mortality-2000","inf-mortality-2010","MHDI-2000","MHDI-2010",\
                 "MHDI-income-2000","MHDI-income-2010","MHDI-life-ex-2000",\
                 "MHDI-life-ex-2010","MHDI-education-2000","MHDI-education-2010",\
                 "education-2000","education-2010","income-2000","income-2010"]

# use data from 1991, 2000, 2010
# cities  = functions.import_data("data_cities.csv", columns, 5567)
states = functions.import_data("data_states.csv", columns, 29)
# use data from 2000, 2010
MAs     = functions.import_data("data_metro_areas.csv", columns_small, 22)
regions = functions.import_data("data_regional_divisions.csv", columns_small, 187) 
chdir("/home/cree/workspace/econometrics/")