# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:35:44 2022

@author: Carlos
"""

import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib


datos = pd.read_csv("mamografia.csv", sep=",")
figure, axes = plt.subplots(2,2, constrained_layout=True)
axes[0, 0].set_title("subplot 1")

ax = plt.subplot(2, 3, 1)
x = datos["class"].value_counts().index.tolist()
y = datos["class"].value_counts().tolist()
ax.bar(x,y)
ax.set_xlabel('tipo')
ax.set_ylabel('cantidad')
ax.set_title('BI-RADS')

ax = plt.subplot(2, 3, 2)
x1 = datos["age"].value_counts().index.tolist()
y1 = datos["age"].value_counts().tolist()
ax.bar(x1,y1)
ax.set_xlabel('edad')
ax.set_ylabel('cantidad')
ax.set_title('EDAD')

ax = plt.subplot(2, 3, 3)
x1 = datos["shape"].value_counts().index.tolist()
y1 = datos["shape"].value_counts().tolist()
ax.bar(x1,y1)
ax.bar(x1,y1)
ax.set_xlabel('forma')
ax.set_ylabel('cantidad')
ax.set_title('FORMA MASA')

ax = plt.subplot(2, 3, 4)
x1 = datos["margin"].value_counts().index.tolist()
y1 = datos["margin"].value_counts().tolist()
ax.bar(x1,y1)
ax.set_xlabel('margen')
ax.set_ylabel('cantidad')
ax.set_title('MARGEN DE MASA')


ax = plt.subplot(2, 3, 5)
x1 = datos["density"].value_counts().index.tolist()
y1 = datos["density"].value_counts().tolist()
ax.bar(x1,y1)
ax.set_xlabel('densidad')
ax.set_ylabel('cantidad')
ax.set_title('DENSIDAD')


ax = plt.subplot(2, 3, 6)
x1 = datos["severity"].value_counts().index.tolist()
y1 = datos["severity"].value_counts().tolist()
ax.bar(x1,y1)
ax.set_xlabel('gravedad')
ax.set_ylabel('cantidad')
ax.set_title('GRAVEDAD')


