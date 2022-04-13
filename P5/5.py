# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:26:19 2022

@author: Carlos
"""
"""
import pandas as pd
datos = pd.read_csv("mamografia1.csv", index_col = 0)


X = datos.iloc[:,[0,1,2,3]]
Y = datos.iloc[:,[4]]


from sklearn import tree 
arbol = tree.DecisionTreeClassifier()
arbol.fit(X,Y)


from matplotlib import pyplot as plt
tree.plot_tree(decision_tree=arbol, feature_names=list(X.columns.values),class_names=list(Y.values), filled=True)
plt.show()
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from pylab import rcParams
rcParams['figure.figsize']=30,30

dataset = pd.read_csv("mamografia1.csv", header=None)

X = dataset.drop([0,1,2,3],axis=1)
y= dataset[4]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20)
classifier = DecisionTreeClassifier()
classifier = classifier.fit(X_train, y_train)
plot_tree(classifier,filled=True)

plt.show()

