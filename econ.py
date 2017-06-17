import functions
import data
import pandas as pd
import numpy as np
import statsmodels.api as sm


renda, ensino = functions.data_prep(data.state_renda, data.state_ensino)
rendaXensino = sm.OLS(ensino.loc['Santa Catarina'], renda.loc['Santa Catarina'], missing='drop').fit()
print(rendaXensino.summary())
rendaXensino = sm.OLS(ensino['1993'], renda['1993'], missing='drop').fit()
print(rendaXensino.summary())
# for row in renda.itertuples():
	# rendaXensino = sm.OLS(ensino.loc[row[0]], renda.loc['Santa Catarina'], missing='drop').fit()
	# print(rendaXensino.summary())
## cant compare 2 large tables like this... need to grab cities and states ONE BY ONE and compare them?


# #OLS functions
# functions.OLS(data.municipio_renda,data.municipio_ensino)
# functions.OLS(data.municipio_ensino,data.municipio_saude)
# functions.OLS(data.municipio_saude,data.municipio_renda)
# functions.OLS(data.state_renda,data.state_ensino)
# functions.OLS(data.state_saude,data.state_ensino)
# functions.OLS(data.state_renda,data.state_saude)