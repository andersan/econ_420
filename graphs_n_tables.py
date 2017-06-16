import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data
import functions
from matplotlib.font_manager import FontProperties
from tabulate import tabulate

# fontP = FontProperties()
# fontP.set_size('small')


# # plot states
# dc = data.state_renda.copy()
# dc.set_index('Estado', inplace=True)
# years = functions.years(dc)
# for values in dc.values:
# 	plt.plot(years, np.delete(values, [0,1]))


# plt.title("Income by state")
# plt.xlabel("Year")
# plt.ylabel("Per capita monthly family income")	
# plt.legend(dc.index.astype(str), loc='center left', bbox_to_anchor=(1, 0.5), prop = fontP)

# plt.show()

# state renda
# functions.graph(data.state_renda, "Income by state", "Year", "Per capita monthly family income (average)", "Estado")

# state ensino
# functions.graph(data.state_ensino, "Years of schooling by state", "Year of census", "Years of schooling (average)", "Estado")

# state saude
# functions.graph(data.state_saude, "Infant mortality", "Year", "Deaths per 1000 births", "Estado")

# descriptive statistics on data
df = data.state_saude.drop(['Código','Sigla'], axis=1)
df.loc['mean'] = df.mean()
df['Estado']['mean'] = 'Mean'

print(tabulate(df, headers='keys', tablefmt='latex', showindex=False, floatfmt=".2f"))

df = data.state_renda.drop(['Código','Sigla'], axis=1)
df.loc['mean'] = df.mean()
df['Estado']['mean'] = 'Mean'

print(tabulate(df.iloc[:,:3].join(df.iloc[:,33:]), headers='keys', tablefmt='latex', showindex=False, floatfmt=".2f"))

df = data.state_ensino.drop(['Código','Sigla'], axis=1)
df.loc['mean'] = df.mean()
df['Estado']['mean'] = 'Mean'

print(tabulate(df.iloc[:,:3].join(df.iloc[:,29:]), headers='keys', tablefmt='latex', showindex=False, floatfmt=".2f"))
