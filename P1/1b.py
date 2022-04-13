# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:09:33 2022

@author: Carlos
"""

import pandas as pd
import numpy as np
datos = pd.read_csv("mamografia.csv")
mamografia = pd.read_csv("mamografia.csv", sep=",")

print("1er Cuartil")
l=[]
l =datos["age"].tolist()

lista = [x for x in l if np.isnan(x) == False]
lista.sort()
age = np.quantile(lista,0.25)
print("Edad:",age)

l=[]
l =datos["shape"].tolist()

lista = [x for x in l if np.isnan(x) == False]
lista.sort()
shape = np.quantile(lista,0.25)
print("Forma de la masa:",shape)

l=[]
l =datos["margin"].tolist()

lista = [x for x in l if np.isnan(x) == False]
lista.sort()
margin = np.quantile(lista,0.25)
print("Margen:",margin)

l=[]
l =datos["density"].tolist()

lista = [x for x in l if np.isnan(x) == False]
lista.sort()
density = np.quantile(lista,0.25)
print("Densidad:",density)

l=[]
l =datos["severity"].tolist()

lista = [x for x in l if np.isnan(x) == False]
lista.sort()
severity = np.quantile(lista,0.25)
print("Garvedad:",severity)
print("-----------------------------------------------------")
print("Percentil 50")

l=[]
l =datos["age"].tolist()

lista = [x for x in l if np.isnan(x) == False]
lista.sort()
age = np.percentile(lista,50)
print("Edad:",age)

l=[]
l =datos["shape"].tolist()

lista = [x for x in l if np.isnan(x) == False]
lista.sort()
shape = np.percentile(lista,50)
print("Forma de la masa:",shape)

l=[]
l =datos["margin"].tolist()

lista = [x for x in l if np.isnan(x) == False]
lista.sort()
margin = np.percentile(lista,50)
print("Margen:",margin)

l=[]
l =datos["density"].tolist()

lista = [x for x in l if np.isnan(x) == False]
lista.sort()
density = np.percentile(lista,50)
print("Densidad:",density)

l=[]
l =datos["severity"].tolist()

lista = [x for x in l if np.isnan(x) == False]
lista.sort()
severity = np.percentile(lista,50)
print("Gravedad:",severity)


