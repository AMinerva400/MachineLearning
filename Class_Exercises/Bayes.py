#!/usr/bin/python
#Author: Anthony Minerva
#Date: September 24th, 2018
#Desc: Naive Bayes with SKLearn

from sklearn.naive_bayes import GaussianNB
import numpy as np

#Setup our Features and Labels
	#Features for Height and Weight
X = np.array([ [5.5, 145], [6.1, 290], [5.6, 210], [4.4, 110], [5.9, 180] ])
	#Healthy: 1 = Yes, 2 = No
Y = np.array([1, 0, 0, 1, 1])

#Create our Classifier
clf = GaussianNB()

#Fit our Classifier (Train it with our current dataset)
clf.fit(X, Y)

pred = clf.predict([ [5.1, 200], [6.2, 100], [4.4, 200], [5.6, 205] ])
print pred

