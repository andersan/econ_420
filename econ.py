import functions
import data
from os import chdir
import matplotlib.pyplot as plt
import pandas as pd


#descriptive statistics
for i in vars(data):
	if "state_" in i or "municipio_" in i:
		print(i)
		print(type(vars(data)[i]))
#data visualization
dc = data.state_saude
data.state_saude.dtypes
plt.plot(dc)
plt.legend(dc.columns)
dcsummary = pd.DataFrame([dc.mean(), dc.sum()],index=['Mean','Total'])

plt.table(cellText=dcsummary.values,colWidths = [0.25]*len(dc.columns),
          rowLabels=dcsummary.index,
          colLabels=dcsummary.columns,
          cellLoc = 'center', rowLoc = 'center',
          loc='top')
fig = plt.gcf()

plt.show()

# #OLS functions
# functions.OLS(data.municipio_renda,data.municipio_ensino)
# functions.OLS(data.municipio_ensino,data.municipio_saude)
# functions.OLS(data.municipio_saude,data.municipio_renda)
# functions.OLS(data.state_renda,data.state_ensino)
# functions.OLS(data.state_saude,data.state_ensino)
# functions.OLS(data.state_renda,data.state_saude)