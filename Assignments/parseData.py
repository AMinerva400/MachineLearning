#!/usr/bin/python
#Author: Anthony Minerva
#Date: October 21st, 2018
#Desc: Read a CSV file of tweets and separate them into a Training and Test Set

import csv
import pandas as pd

fileName = 'fullTweets.csv'

def readCSV(f):
        df = pd.read_csv(f)
        return df

def createSets(df):
	trainingSet = df.sample(200)
	testSet = df.loc[~df.index.isin(trainingSet.index)]
	trainingSet.to_csv('trainingTweets.csv')
	testSet.to_csv('testTweets.csv')

createSets(readCSV(fileName))
