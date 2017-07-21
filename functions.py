import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import statsmodels.api as sm
import statsmodels.formula.api as smf
from matplotlib.font_manager import FontProperties
import seaborn as sns


'''
this file creates methods to be used in the rest of the project.
those methods include:
import_data(file, column names, rows): import data to pandas dataframes from csvs
OLS: run an OLS on the two dataframes that are included. automagically runs
      on all of the correct columns
'''

# styles for any print/graph methods
legendFont = FontProperties()
legendFont.set_size('small')
legendFont.set_family('serif')
serifFont = {'fontname':'Times New Roman'}

# import all CSV files with data into python
# TODO: refactor code to make "year" sorting/dataset shifting optional... this will make this code more useful in the future
def import_data (filename, columns, num_rows):
  df = pd.read_csv(filename, sep=';', names = columns, decimal=',', encoding = "ISO-8859-1")
  df = df.drop(0) # drop row of indicator names, use column names instead
  # loop over every column in df
  df['year'] = None
  # create dataframe so DF can just be iterated over
  store = df.copy()
  for col in df.iloc[:,3:len(columns)]:
    # make data usable as a float (numeric value) when using commas
    # df[col] = pd.to_numeric(df[col].str.replace(',','.'))
    year = int(col[-4:])
    colName = col[:-5]
    for index,entry in df[col].iteritems():
      locale = store.loc[index,'locale']
      if  ((store['locale'] == locale) & (store['year'] == year)).any():
        index_1 = store[(store['locale'] == locale)&(store['year'] == year)].index
        store.set_value(index_1[0], colName, entry)
      else:
        # new row
        df2 = pd.DataFrame([[entry,locale,year]], columns=[col[:-5],'locale','year'])
        store = store.append(df2, ignore_index=True)# add this data to pandas dataframe
    # drop indicator-year column, data has been moved to a 'year' var and an indicator var
    store = store.drop(col, axis=1)
  print(store, store.columns)
  # cut empty rows from dataframe
  slice_index = num_rows - 1
  store = store[slice_index:].reset_index(drop=True)
  # export dataframe to csv - can load faster for analysis
  store.to_csv('formatted_' + filename)
  return store;

def sns_graph(df,title,xvar,xaxis,yvar,yaxis):
  sns.regplot(x=xvar, y=yvar, line_kws={"color": "g"}, data=df)
  sns.plt.xlabel(xaxis,**serifFont, fontsize=12)
  sns.plt.ylabel(yaxis,**serifFont, fontsize=12)
  sns.plt.title(title,**serifFont, fontsize=14)
  sns.plt.savefig('{xvar}{yvar}'.format(xvar=xvar,yvar=yvar), bbox_inches='tight')
  # sns.plt.show()
  sns.plt.close()

def rsquared(df, formulas):
  results = {}
  for f in formulas:
    ols = smf.ols(f, data=df).fit()
    results[f] = ols.rsquared
  return results;
  
def params(df, formulas):
  results = {}
  for f in formulas:
    ols = smf.ols(f, data=df).fit()
    results[f] = ols.params
  return results;