import pandas as pd
import numpy as np
from os import chdir
import statsmodels.api as sm
import test

chdir("/home/cree/Downloads/br_econ/")

# municipal: loop through income and years of study
test.OLS(test.df,test.df1)

# municipal: loop through infant mortality and years of study
test.OLS(test.df1,test.df2)

# municipal: loop through income and infant mortality
test.OLS(test.df,test.df2)

# state: loop through income and years of study
test.OLS(test.df4,test.df5)

# state: loop through infant mortality and years of study
test.OLS(test.df5,test.df9)

# state: loop through income and infant mortality
test.OLS(test.df4,test.df9)