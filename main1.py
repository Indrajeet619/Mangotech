import datetime as dt

import pandas as pd
import numpy as np
import seaborn as sns
import requests
import matplotlib.pyplot as plt
%matplotlib inline 

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import RandomizedSearchCV


daynight_map = {"D": 1, "N": 0}
satellite_map = {"Terra": 1, "Aqua": 0}

forest['daynight'] = forest['daynight'].map(daynight_map)
forest['satellite'] = forest['satellite'].map(satellite_map)
types = pd.get_dummies(forest['type'])
forest = pd.concat([forest, types], axis=1)
forest = forest.drop(['type'], axis = 1)
forest.head()
forest = forest.rename(columns={0: 'type_0', 2: 'type_2', 3: 'type_3'})
bins = [0, 1, 2, 3, 4, 5]
labels = [1,2,3,4,5]
forest['scan_binned'] = pd.cut(forest['scan'], bins=bins, labels=labels)
y = forest['confidence']
fin = forest.drop(['confidence', 'acq_date', 'acq_time', 'bright_t31', 'type_0'], axis = 1)
Xtrain, Xtest, ytrain, ytest = train_test_split(fin.iloc[:, :500], y, test_size=0.2)
random_model.get_params()
"""
n_estimators = number of trees in the forest
max_features = max number of features considered for splitting a node
max_depth = max number of levels in each decision tree
min_samples_split = min number of data points placed in a node before the node is split
min_samples_leaf = min number of data points allowed in a leaf node
bootstrap = method for sampling data points (with or without replacement)
"""
n_estimators = [int(x) for x in np.linspace(start = 300, stop = 500, num = 20)]
Number of features to consider at every split
max_features = ['auto', 'sqrt']
Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(15, 35, num = 7)]
max_depth.append(None)
Minimum number of samples required to split a node
min_samples_split = [2, 3, 5]
Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
                }
print(random_grid)
rf_random = RandomizedSearchCV(estimator = random_model, param_distributions = random_grid, 
                                n_iter = 50, cv = 3, verbose=2, random_state=42)
rf_random.fit(Xtrain, ytrain)
rf_random.best_params_
random_new = RandomForestRegressor(n_estimators = 394, min_samples_split = 2, min_samples_leaf = 1, max_features = 'sqrt',
                                      max_depth = 25, bootstrap = True)
                                      random_new.fit(Xtrain, ytrain)
y_pred1 = random_new.predict(Xtest)
random_model_accuracy1 = round(random_new.score(Xtrain, ytrain)*100,2)
print(round(random_model_accuracy1, 2), '%')
Month=random_new[0]
Day=random_new[1]
Long=random_new[2]
Prob=random_new[3]

pload = {'Month':Month,'Day':Day,'Longitude ':Long,'Probability':Prob}
r = requests.post('https://mangotech.com/post',data = pload)
  
r = requests.post(url = API_ENDPOINT, data = data)
  