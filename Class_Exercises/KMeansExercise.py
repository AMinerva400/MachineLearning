#!/usr/bin/python
#Author: Anthony Minerva
#Date: November 5th
#Desc: K-Means Exercise

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def runKMeans(X, k):
	km = KMeans(n_clusters=k, random_state=0, verbose = 0)
	km.fit(X)
	labels = km.labels_
	return labels, km.inertia_

def makeDataFrame(X, y, cols):
	ds = list(zip(X, y))
	cols = cols.split(",")
	df = pd.DataFrame(ds, columns = cols)
	return df

def main():
	featureTrain = np.array([
		[1,4],
		[-3,0],
		[5,0],
		[1,-4],
		[-6,17],
		[-10,13],
		[-2,-13],
		[-6,9],
		[10,15],
		[6,11],
		[14,11],
		[10,7],
	])
	sseList = []
	print "\nPrinting out the SSE to find optimal k - clusters"
	for i in range(1, 10, 1):
		featureLabels, sse = runKMeans(featureTrain, i)
		print i, "%.2f" % sse
		sseList.append([i,sse])
		if sse <= 0:
			break
	k = 3
	df_featureLabels = makeDataFrame(featureTrain, featureLabels, "Features, Labels")
	print "\nPrint our features and labels\n", df_featureLabels

main()
