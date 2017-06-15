import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import chdir
import glob
import statsmodels.api as sm

'''
this file creates methods to be used in the rest of the project.
those methods include:
import_data(folder): import data to pandas dataframes from csvs
OLS: run an OLS on the two dataframes that are included. automagically runs 
			on all of the correct columns
''' 


chdir("/home/cree/Downloads/br_econ/")
mun, state = {}, {}

# import all CSV files with data into python  
def import_data (folder_name):
	dictionary = {}
	for filename in glob.glob(folder_name+"/*.csv"):
		# read CSV file into Pandas dataframe
		store = pd.read_csv(filename, sep=';')
		# store dataframe in a list of values, deleting empty columns from dataset
		dictionary[filename] = store.dropna(axis=1,how='all')
	return dictionary

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

chdir("/home/cree/workspace/econometrics/")
