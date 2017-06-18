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
def import_data (folder_name):
  dictionary = {}
  for filename in glob.glob(folder_name+"/*.csv"):
    # read CSV file into Pandas dataframe
    store = pd.read_csv(filename, sep=';')
    # store dataframe in a list of values, deleting empty columns from dataset
    dictionary[filename] = store.dropna(axis=1,how='all')
  return dictionary

def data_prep(df):
  # drop unused rows
  df = df.transpose()
  # set state names and city codes as column labels, drop unused rows
  if 'Estado' in df.index:
    df.columns = df.iloc[2]
    df = df.drop(['Código','Sigla','Estado'])
  elif 'Município' in df.index:
    df.columns = df.iloc[1]
    df = df.drop(['Código','Sigla','Município'])
  df.columns.names = ['']
  # create year column 
  df['Year'] = df.index
  # df.index = range(len(df.index))
  return df;

def numpy_to_pd(df):
  for col in df:
    try:
      df[col] = pd.to_numeric(df[col])
    except:
      for col in df[col]:
        print(col) 
  return df;

# input 2 dataframes, output OLS results for ALL SHARED YEARS 
def OLS(df1, df2):
  # catch anual datasets
  if len(df1.columns) > 10 and len(df2.columns) > 10:
    years = [str(x) for x in range(1970,2014)]
    for year in years:
      for col1 in df1:
        if year in col1:
          for col2 in df2:
            if year in col2:
              #print(year,col1,col2) 
              continue;
              #DO OLS OPERATION ON 2 COLUMNS
              # STORE OLS
  # catch census datasets
  else:
    years = ("1970", "1980", "1991", "2000") # years census was conducted
    for year in years:
      for col1 in df1:
        if year in col1:
          for col2 in df2:
            if year in col2:
              #print(year,col1,col2) 
              continue;
              #DO OLS OPERATION ON 2 COLUMNS
              # STORE OLS
    # return all OLS
  return;

# return years used in dataset, taken from column headers
def years(df):
  years = []
  for i in df['Year']:
    try:
      years.append(int(i))
    except:
      continue;
  return years;

def compare_years(df1, df2):
  #determine what years of data are shared across dataframes
  shared_years = [val for val in years(df1) if val in years(df2)]
  for y in df1['Year']:
    if int(y) not in shared_years:
      mask = df1['Year'] == y
      first, df1 = df1[mask], df1[~mask]
      # df1 = df1.drop(y)
  for y in df2['Year']:
    if int(y) not in shared_years:
      mask = df2['Year'] == y
      first, df2 = df2[mask], df2[~mask]
      # df2 = df2.drop(y)
  return df1, df2


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

