import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import chdir
import glob

chdir("/home/cree/Downloads/br_econ/")
count = 0
mun, state = {}, {}

# input data to pandas dataframes
for filename in glob.glob("mun/*.csv"):
	mun[filename] = pd.read_csv(filename, sep=';')

a = [value for key, value in mun.items() if 'familiar' in key.lower()]
renda_familiar = pd.merge(pd.merge(pd.merge(a[0], a[1], on=["Sigla", "Código","Município"]), a[2], on=["Sigla", "Código","Município"]), a[3], on=["Sigla", "Código","Município"])
renda_familiar = renda_familiar.dropna(axis=1,how='all')
