#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:54:38 2018

@author: nishant
"""

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Importing the dataset

dataset = pd.read_csv('train.csv')

X = dataset.iloc[0:3000000, 4:25].values
y = dataset.iloc[0:3000000, 25:26].values
X_test = dataset.iloc[3000000:4357336, 4:25].values
y_test = dataset.iloc[3000000:4357336, 25:26].values

# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

# Predicting a new result
y_pred = regressor.predict(X_test)

#r squared val
from sklearn.metrics import r2_score
r2= r2_score(y_test, y_pred)  
adj_r2= r2- (20/4357336)*(1-r2)

# Visualising the Test set results
plt.scatter(y_test, y_pred, color = 'red',  alpha=0.004)
plt.title('qq for all test cases')
plt.xlabel('y_test')
plt.ylabel('y_pred')
plt.show()


##############################################################
####             saving and loading a model               ####
##############################################################

#saving model
filename = 'final_model2.sav'
pickle.dump(regressor, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

#predict from loaded model
y_pred = loaded_model.predict(X_test)
