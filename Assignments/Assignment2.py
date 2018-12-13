#!/usr/bin/python
#Author: Anthony Minerva
#Date: December 5th
#Desc: Assignment 2: Analyzing Crimes with K-Nearest Neighbor

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

fileName = "ChicagoCrimes.csv"

def readCSV(fileName):
	df = pd.read_csv(fileName)
	return df

def KM(X, k):
	km = KMeans(n_clusters=k, random_state=0, verbose=0)
	km.fit(X)
	return km

def runKMeans(X, k):
	km = KM(X, k)
	labels = km.labels_
	return labels, km.inertia_

def plotElbow(sseList):
	plt.plot(sseList, marker='o')
	plt.xlabel("Clusters")
	plt.ylabel("SSE")
	plt.show()

def plotCluster(X, k, Arrests):
	ar = 0.0
	noAr = 0.0
	for i in range (0, len(Arrests)):
		if Arrests[i]:
			ar = ar + 1
		else:
			noAr = noAr + 1
	acc = 100 * (ar / (ar+noAr))
	print "Percent of Encounters Resulting in Arrest:", str(acc)
	print "Encounters: ", str(len(Arrests))
	km = KM(X, k)
	yKM = km.predict(X)
	colors = ['blue', 'yellow', 'green']
	marks = ['o', 'x', 'v']
	plt.xlabel("Latitude")
	plt.xlim(41.6, 42.2)
	plt.ylim(-88, -87.4)
	plt.ylabel("Longitude")
	for i in range(0, k):
		plt.scatter(X.iloc[yKM == i, 0], X.iloc[yKM == i, 1], c=colors[i], marker= (marks[0] if Arrests else marks[1]))
	plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], marker='*', c='red')
	plt.grid()
	plt.show()

def run():
	df = readCSV(fileName)
	dataFrame = df[df.Description.str.contains("CANNABIS")]
	year = raw_input("Enter a year between 2001 and 2015, or -1 for a yearly analysis: ")
	if int(year) >= 2001 and int(year) <= 2015:
		dataFrame = dataFrame[dataFrame['Year'] == int(year)]
		ar = list(dataFrame.Arrest.values)
		print "Data restricted to ", year
	featureTrain = dataFrame[dataFrame.Latitude.notnull() & dataFrame.Longitude.notnull()][['Latitude', 'Longitude']]
	sseList = []
	#Find Optimal K-Clusters with Elbow Method
        print "\nPrinting out the SSE to find optimal k - clusters"
        for i in range(1, 10, 1):
                featureLabels, sse = runKMeans(featureTrain, i)
                print i, "%.2f" % sse
                sseList.append(sse)
                if sse <= 0:
                        break
	#Plots SSE Data to show Optimal K-Clusters
	plotElbow(sseList)
	#In this case, 2 is the optimal K, and has been hard-coded
	k = 2
	print "\nOptimal Number Of Clusters: ", k
	if int(year) == -1: #If User specified Yearly Analysis - Compute Said Analysis
		for i in range(2001, 2016): #Range from 2001 to 2015 (End value not inclusive)
			print "\nAnalyzing ", i
			yearlyData = dataFrame[dataFrame['Year'] == i]
			featureTrain = yearlyData[yearlyData.Latitude.notnull() & yearlyData.Longitude.notnull()][['Latitude', 'Longitude']]
			#Specify Labels and Title
			plt.title("Analysis of Cannabis-Related Crimes in "+ str(i))
			plotCluster(featureTrain, k, list(yearlyData.Arrest.values))
		print "In general, most years showed a relatively similar clustering - with the exception of 2011, which generally showed 1 cluster (Most likely due to outlier values in the Data Set)"
	else: #If User Specified a Year - Provide the Analysis for that Specific Year, with K-Clusters
		plt.title("Analysis of Cannabis-Related Crimes in " + year)
		plotCluster(featureTrain, k, ar)

run()


