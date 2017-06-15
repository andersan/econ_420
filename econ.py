import pandas as pd
import numpy as np
from os import chdir
import statsmodels.api as sm
import data

chdir("/home/cree/Downloads/br_econ/")

# municipal: loop through income and years of study
test.OLS(test.municipio_renda,test.municipio_ensino)

# municipal: loop through infant mortality and years of study
test.OLS(test.municipio_ensino,test.municipio_saude)

# municipal: loop through income and infant mortality
test.OLS(test.municipio_saude,test.municipio_renda)

# state: loop through income and years of study
test.OLS(test.state_renda,test.state_ensino)

# state: loop through infant mortality and years of study
test.OLS(test.state_saude,test.state_ensino)

# state: loop through income and infant mortality
test.OLS(test.state_renda,test.state_saude)