# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 19:51:12 2022

@author: Carlos
"""

import csv
file = open('mamografia.csv')
type(file)
csvreader = csv.reader(file)

cabeza=[]
cabeza=next(csvreader)
cabeza

columnas=[]

for col in csvreader:
    columnas.append(col)

biRads=[]
i=0
for j in columnas:
    biRads.append(columnas[i][5])
    i=i+1
#print(biRads)
age=[]
i=0
for j in columnas:
    age.append(columnas[i][0])
    i=i+1
#print(age)
shape=[]
i=0
for j in columnas:
    shape.append(columnas[i][1])
    i=i+1
#print(shape)
margin=[]
i=0
for j in columnas:
    margin.append(columnas[i][2])
    i=i+1
#print(margin)
density=[]
i=0
for j in columnas:
    density.append(columnas[i][3])
    i=i+1
#print(density)
severity=[]
i=0
for j in columnas:
    severity.append(columnas[i][4])
    i=i+1

#print(severity)


import math
for i in age:
    if i =='':
        age.remove(i)
for j in shape:
    if j =='':
        shape.remove(j)
for i in margin:
    if i =='':
        margin.remove(i)
for i in density:
    if i =='':
        density.remove(i)
for i in severity:
    if i =='':
        severity.remove(i)
        

biRads.sort()
age.sort()
shape.sort()
margin.sort()
density.sort()
severity.sort()

n =  len(biRads)
# para el el primer cuartil
# usamos la formula k*(n+1)/4
# donde k=1 y n = 961
z = (n+1)/4
p_dec, p_ent = math.modf(z)
p_ent = int(p_ent)
#interpolamos ya que el resultado tiene decimales
dato1 = int(age[p_ent])
dato2 = int(age[p_ent+1])
qAge= dato1+(p_dec*(dato2-dato1))
print("EDAD")
print(qAge)
print("El 25% de la poblacion de datos tiene ",qAge," años o menos")
print("-------------------------------------------------------------")
dato1 = int(shape[p_ent])
dato2 = int(shape[p_ent+1])
qShape= dato1+(p_dec*(dato2-dato1))
print("FORMA DE MASA")
print(qShape)
print("En el primer cuartil de datos se presentan 2 tipos de forma de la masa que son 'Redonda y 'Ovalada'' ")
print("-------------------------------------------------------------")
dato1 = int(margin[p_ent])
dato2 = int(margin[p_ent+1])
qMargin = dato1+(p_dec*(dato2-dato1))
print("MARGEN DE MASA")
print(qMargin)
print("En el primer cuartil de datos se presenta el margen de la masa: 'Circunscrito'")
print("-------------------------------------------------------------")
dato1 = int(density[p_ent])
dato2 = int(density[p_ent+1])
qDen = dato1+(p_dec*(dato2-dato1))
print("DENSIDAD")
print(qDen)
print("En el primer cuartil de datos se presentan 3 tipos de densidad de la masa ´Denisdad de Masa alto´, 'Iso' y 'Baja''")
print("-------------------------------------------------------------")
dato1 = int(severity[p_ent])
dato2 = int(severity[p_ent+1])
qSev = dato1+(p_dec*(dato2-dato1))
print('GRAVEDAD')
print(qSev)
print("En el primer cuartil de datos se presenta que la gravedad de los casos es de tipo 'Benigno''")
print("-------------------------------------------------------------")

# para el el primer cuartil
# usamos la formula k*(n+1)/100
# donde k=1 y n=961
z = (50*(n+1))/100
print("-------------------------------------------------------------")
print("-------------------------------------------------------------")
print("PERCENTIL 50")
print("EDAD")
print(age[int(z)])
print("El 50% de la poblacion de datos tiene ",age[int(z)]," años o menos")
print("-------------------------------------------------------------")
print("FORMA DE MASA")
print(shape[int(z)])
print("50 % de datos se presentan entre 3 tipos de forma de la masa que son 'Redonda' ,'Ovalada' y 'Lobular' ")
print("-------------------------------------------------------------")
print("MARGEN DE MASA")
print(margin[int(z)])
print("50 % de datos se presentan entre 3 tipos de margen de la masa: 'Circunscrito','Microbulado' y 'Oscurecido'")
print("-------------------------------------------------------------")
print("DENSIDAD")
print(density[int(z)])
print("50 % de datos se presentan entre 3 tipos de densidad de la masa ´Denisdad de Masa alto´, 'Iso' y 'Baja''")
print("-------------------------------------------------------------")
print('GRAVEDAD')
print(severity[int(z)])
print("50 % de datos presenta que la gravedad de los casos es de tipo 'Benigno''")







