#!/usr/bin/python
#Author: Anthony Minerva
#Date: September 24th, 2018
#Desc: Class Exercise 6: Sports Bayes

import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

filename = 'sports_class.csv'

def readCSV(f):
	df = pd.read_csv(f)
	return df

def fitData(df):
	X = df[['Height', 'Speed']]
	Y = df[['Class']]
	clf = GaussianNB()
	clf.fit(X, np.ravel(Y))
	return clf

def predict(clf, data):
	pred = clf.predict(data)
	print pred

df = readCSV(filename)
clf = fitData(df)
predict(clf, [ [5.2, 17], [7.9, 12], [4.4, 13] ])

