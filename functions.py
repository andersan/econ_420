import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import chdir
import glob
import statsmodels.api as sm
from matplotlib.font_manager import FontProperties


'''
this file creates methods to be used in the rest of the project.
those methods include:
import_data(folder): import data to pandas dataframes from csvs
OLS: run an OLS on the two dataframes that are included. automagically runs 
      on all of the correct columns
'''

# import all CSV files with data into python  
# TODO: refactor code to make "year" sorting/dataset shifting optional 
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

def data_prep(df):
  # nothing?
  return df;

def graph(dataframe, graph_title, x_axis_title, y_axis_title, index_var):
  legendFont = FontProperties()
  legendFont.set_size('small')
  legendFont.set_family('serif')
  serifFont = {'fontname':'Times New Roman'}


  # plot states
  dc = dataframe.copy()
  dc.set_index(index_var, inplace=True)
  yrs = years(dc)
  for values in dc.values:
    plt.plot(yrs, np.delete(values, [0,1]))


  plt.title(graph_title,**serifFont, fontsize=14)
  plt.xlabel(x_axis_title, **serifFont, fontsize=12)
  plt.ylabel(y_axis_title, **serifFont, fontsize=12)
  plt.legend(dc.index.astype(str), loc='center left', bbox_to_anchor=(1, 0.5), prop = legendFont)

  plt.show()

