import functions
import data
from os import chdir

#descriptive statistics
for i in vars(data):
	if "state_" in i or "municipio_" in i:
		print(i)
		print(type(vars(data)[i]))
#data visualization

#OLS functions
functions.OLS(data.municipio_renda,data.municipio_ensino)
functions.OLS(data.municipio_ensino,data.municipio_saude)
functions.OLS(data.municipio_saude,data.municipio_renda)
functions.OLS(data.state_renda,data.state_ensino)
functions.OLS(data.state_saude,data.state_ensino)
functions.OLS(data.state_renda,data.state_saude)