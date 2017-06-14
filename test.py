import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import chdir
import glob

chdir("/home/cree/Downloads/br_econ/")
count = 0
mun, state = {}, {}

# import all CSV files with data into python  
def dataframe (folder_name):
	dictionary = {}
	for filename in glob.glob(folder_name+"/*.csv"):
		# read CSV file into Pandas dataframe
		store = pd.read_csv(filename, sep=';')
		# store dataframe in a list of values, deleting empty columns from dataset
		dictionary[filename] = store.dropna(axis=1,how='all')
	return dictionary

mun = dataframe("mun")
state = dataframe("state")

#rename columns
# mun.get('mun/Renda_municipios - Renda familiar - per capita - média.csv').columns
# df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)



# merge like datasets in pandas
# search for keys in mun(icipal) dictionary that match the filename strings
# merged files manually... but this code works, albiet with illogical ordering of columns
	# by alphabetical filename instead of by the year of the data.

# a = [value for key, value in mun.items() if 'familiar' in key.lower()]
# renda_familiar = pd.merge(pd.merge(pd.merge(a[0], a[1], on=["Sigla", "Código","Município"]), a[2], on=["Sigla", "Código","Município"]), a[3], on=["Sigla", "Código","Município"])
# renda_familiar = renda_familiar.dropna(axis=1,how='all')

# a = [value for key, value in mun.items() if 'mun_media' in key.lower()]
# renda_familiar = pd.merge(pd.merge(pd.merge(a[0], a[1], on=["Sigla", "Código","Município"]), a[2], on=["Sigla", "Código","Município"]), a[3], on=["Sigla", "Código","Município"])
# renda_familiar = renda_familiar.dropna(axis=1,how='all')