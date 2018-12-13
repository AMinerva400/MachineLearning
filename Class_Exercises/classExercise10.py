#!/usr/bin/python
#Author: Anthony Minerva
#Date: November 5th, 2018
#Desc: Class Exercise 10: K-Means

from sklearn.cluster import KMeans
import pandas as pd
import numpy as nm

#fit(X[ ['s_length', 's_width']])
#labels = KM.predict(X[['s_length', 's_width']])
#inertia is basically the SSE

fileName = "irisdata.csv"

def runKMeans(X, k):
        km = KMeans(n_clusters=k, random_state=0, verbose = 0)
        km.fit(X[['s_length', 's_width']])
        labels = km.predict(X[['s_length', 's_width']])
        return labels, km.inertia_

def readCSV(fileName):
	return pd.read_csv(fileName)

def makeDataFrame(X, y, cols):
        ds = list(zip(X, y))
        cols = cols.split(",")
        df = pd.DataFrame(ds, columns = cols)
        return df

def main():
        df = readCSV(fileName)
        sseList = []
        print "\nPrinting out the SSE to find optimal k - clusters"
        for i in range(1, 10, 1):
                featureLabels, sse = runKMeans(df, i)
                print i, "%.2f" % sse
                sseList.append([i,sse])
                if sse <= 0:
                        break
        k = 3

	#Adjust printing part - Also find Graphing to figure out if this is close to the expected results

        df_featureLabels = makeDataFrame(df[['s_length', 's_width']], featureLabels, "Features, Labels")
        print "\nPrint our features and labels\n", df_featureLabels

main()

