#!/usr/bin/python
#Author: Anthony Minerva
#Date: October 1st, 2018
#Desc: Class Exercise 7: Sports SVM

import numpy as np
import pandas as pd
from sklearn.svm import SVC

filename = 'sports_class.csv'


def readCSV(f):
	df = pd.read_csv(f)
	return df

def fitData(df):
	X = df[['Height', 'Speed']]
	Y = df[['Class']]
	clf = SVC(gamma = 'auto')
	clf.fit(X, np.ravel(Y))
	return clf

def predict(clf, data):
	pred = clf.predict(data)
	print pred

df = readCSV(filename)
clf = fitData(df)
predict(clf, [ [5.2, 17], [7.9, 12], [4.4, 13] ])

