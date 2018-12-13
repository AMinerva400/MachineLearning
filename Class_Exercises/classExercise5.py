#!/usr/bin/python
#Author: Anthony Minerva
#Date: September 19th, 2018
#Desc: Class Exercise 5: KNN w/ Iris Data Class

import pandas as pd

filename = 'sports_class.csv'
fileName = 'irisdata.csv'

def readCSV(f):
	df = pd.read_csv(f)
	return df

def calcDistance(x1, y1, x2, y2):
	return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def predict(sLength, sWidth, k):
	df = readCSV(fileName)
	tr = df.sample(100)
	dc = pd.DataFrame(columns = ['Distance', 'Class'])
	for index, row in tr.iterrows():
		dist = calcDistance(row['s_length'], row['s_width'], sLength, sWidth)
		cls = row['class']
		dc = dc.append({'Distance':dist, 'Class':cls}, ignore_index = True)
	#Sort Data
	dc = dc.sort_values(by=['Distance'])
	print '\nk = ' + str(k) + ', The Top-K Nearest Neighbors Are:'
	print dc.head()
	#Take top k items from DataFrame
	top_k = dc.head(k)
	#return top Class only 
	top = top_k['Class'].value_counts().idxmax()
	print 'Predicted: ' + top + ' for length = ' + str(sLength) + ', width = ' + str(sWidth)

predict(5.2, 3.8, 5)
predict(4.2, 2.2, 5)
predict(5.2, 3.8, 7)
predict(4.2, 2.2, 7)
