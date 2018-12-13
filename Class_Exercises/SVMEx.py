#!/usr/bin/python
#Author: Anthony Minerva
#Date: October 1st, 2018
#Desc: SVM Example with SKLearn

import numpy as np
from sklearn.svm import SVC

X = np.array([[-1,-1], [-2,-1], [-3,-2], [1,1], [2,1], [3,2]])
Y = np.array([1,1,1,2,2,2])

clf = SVC(gamma = 'auto')
clf.fit(X,Y)

predict = clf.predict([[-0.8, -1]])
print "The predicted label = ", predict
