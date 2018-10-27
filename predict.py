#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:54:38 2018

@author: nishant
"""

# Importing the libraries

import numpy as np
import pandas as pd
import pickle

# Importing the dataset

dataset = pd.read_csv('train.csv')
testdataset = pd.read_csv('test.csv')

X = dataset.iloc[:, 4:25].values
y = dataset.iloc[:, 25:26].values
X_test = testdataset.iloc[:, 4:25].values
y_test = testdataset.iloc[:, 25:26].values

# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

# Predicting a new result
y_pred = regressor.predict(X_test)

#saving to csv
data=[]
df = pd.DataFrame(data)
df = pd.DataFrame(data,columns=['Id','winPlacePerc'],dtype=float)
df['Id']=testdataset.iloc[:, 0].values
df['winPlacePerc']=y_pred
df.to_csv("sample_submission.csv", sep='\t', encoding='utf-8', index=False)

##############################################################
####             saving and loading a model               ####
##############################################################

#saving model
filename = 'final_model.sav'
pickle.dump(regressor, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

#predict
y_pred = loaded_model.predict(X_test)
