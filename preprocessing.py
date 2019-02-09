# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 16:11:25 2019

@author: Clement_X240
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Read data from csv files
train = pd.read_csv("./datasets/entreprise_1/train.csv")
store = pd.read_csv("./datasets/entreprise_1/store.csv")

# Join the 2 csv files on the Store feature
train_store = pd.merge(train, store, how='inner', on="Store")

del(train)
del(store)

# Replace the '0' values by 0 as StateHoliday is a quantitative feature.
train_store.StateHoliday.replace(0, '0', inplace=True)

# Convert Data feature from object to datetime type.
train_store['Date'] = pd.to_datetime(train_store.Date,
           format='%Y-%m-%d', errors='coerce')

# Complete the CompetitionDistance column values by the median value 
# (replacing NaN values by the median value).
train_store.CompetitionDistance.fillna(train_store.CompetitionDistance.median(), inplace=True)

# Replace the NaN values by 'None'. It will help us to do label encoding below.
train_store.PromoInterval.fillna('None', inplace=True)


# Drop some columns that are not relevant.
train_store = train_store.drop(['CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear','Promo2SinceWeek',
                     'Promo2SinceYear'], axis=1)

# Get Features and Labels
X = train_store.loc[:, train_store.columns != "Sales"]
y = train_store.Sales


##### Label Encoding #####
features_to_encode = ['StoreType', 'Assortment', 'PromoInterval', 'StateHoliday']

encoder = LabelEncoder()

for label in features_to_encode:
    X[label] = encoder.fit_transform(X[label])