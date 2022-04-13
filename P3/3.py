# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:01:32 2022

@author: Carlos
"""
import numpy as np 
import pandas as pd 

datos = pd.read_csv("mamografia.csv")

y = datos.iloc[:,5].values

from sklearn.impute import SimpleImputer
prepro = SimpleImputer(missing_values = np.nan, strategy="mean") 
prepro1 = SimpleImputer(missing_values = np.nan, strategy="most_frequent") 
x1 = np.array(datos.iloc[:, :5].values)
x2 = prepro.fit_transform(x1)
y1 = np.array(datos.iloc[:,5:])
y2 = prepro1.fit_transform(y1)
print(x1)
print(x2)
print(y1)
print(y2)



from sklearn.preprocessing import KBinsDiscretizer
X1 = np.array(x2)
prepro = KBinsDiscretizer(n_bins=4, encode='ordinal', strategy='uniform')
X2 = prepro.fit_transform(X1)
print(X2)


from sklearn.preprocessing import LabelEncoder
lbEncoder = LabelEncoder()
y3 = lbEncoder.fit_transform(y)


