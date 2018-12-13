#!/usr/bin/python
#Author: Anthony Minerva
#Date: October 21th, 2018
#Desc: Assignment 1: Sentiment Analysis with Twitter Feed

import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import time
from sklearn.metrics import accuracy_score
import warnings

#warnings.simplefilter(action='ignore', category=FutureWarning)

fullTweets = 'fullTweets.csv'
trainingTweets = 'trainingTweets.csv'
testTweets = 'testTweets.csv'
vect = CountVectorizer()
generalizedTweets = 'generalizedTweets.csv'

def readCSV(f):
        df = pd.read_csv(f)
        return df

def fitData(df):
        X = df['Tweet']
        Y = df['Sentiment']	
        X = vect.fit_transform(X.values.astype(str))
        clf = MultinomialNB()
        clf.fit(X.toarray() ,np.ravel(Y))
        return clf

def predict(clf, df):
	X = df['Tweet']
	X = vect.transform(X.values.astype(str))
        pred = clf.predict(X.toarray())
	return pred

full = readCSV(fullTweets)
training = readCSV(trainingTweets)
test = readCSV(testTweets)
print 'Hashtags:\n1. #Halloween\n2. #MeToo\n3. #LGBTQ\n'
print training.head(5)
timeA = time.time()
clf = fitData(training)
timeB = time.time()
print 'Training Naive Bayes Model\nTraining Time = ', str(timeB - timeA), 'sec\n'
print test.head(5)
pred = predict(clf, test)
acc = 100*accuracy_score(test['Sentiment'], pred)
print 'Running Test Set\nAccuracy = ', str(acc), '%\n'

print 'Running Generalized Test\nGeneralized Hashtags:\n1. #Thanksgiving\n2. #BlackLivesMatter\n3. #Hofstra\n'
generalized = readCSV(generalizedTweets)
print generalized.head(5)
genPred = predict(clf, generalized)	
gen = [int(i) for i in genPred]
genAcc = 100*accuracy_score(generalized['Sentiment'], gen)
print 'Accuracy = ', str(genAcc), '%\n'
