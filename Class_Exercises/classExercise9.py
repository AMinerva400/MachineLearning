#!/usr/bin/python
#Author: Anthony Minerva
#Date: October 29th, 2018
#Desc: Class Exercise 9 - K Means Exercise

import random
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

allPoints = [ [1,4],[-3,0],[5,0],[1,-4],[-6,17],[-10,13],[-2,13],[-6,9],[10,15],[6,11],[14,11],[10,7] ]

def calcDistance(p1, p2):
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]
	y2 = p2[1]
	return ( (x1 - x2)**2 + (y1 - y2)**2 )**0.5

def assignPoints(Centroids, Classifications, k):
	oldCls = Classifications
	newCls = []
	for i in range(len(allPoints)):
		point = allPoints[i]
		dist = calcDistance(point, Centroids[0])
		cls = 0
		for i in range(k-1):
			d = calcDistance(point, Centroids[i+1])
			if d < dist:
				cls = i+1
				dist = d
		newCls.append(cls)
	return newCls

#Takes List of Classifications and Centroid Associated, Returns Midpoint
def calcMid(cls, c):
	sumX = 0
	xc = 0
	sumY = 0
	yc = 0
	for i in range(len(cls)):
		if cls[i] == c:
			sumX += allPoints[i][0]
			sumY += allPoints[i][1]
			xc += 1
			yc += 1
	return [sumX / xc, sumY / yc]		 

def KMeans(k):
	size = len(allPoints) - 1
	c1 = random.randint(1, size)
	run = True
	while run:
		c2 = random.randint(1, size)
		if c2 != c1:
			run = False
	run = True
	while run:
		c3 = random.randint(1, size)
		if (c3 != c1 ) and (c3 != c2):
			run = False
	oldCls = assignPoints([ allPoints[c1], allPoints[c2], allPoints[c3] ], [], k)
	run = True
	newCls = []
	while run:
		Cents = []
		for i in range(k):
			Cents.append(calcMid(oldCls, i))
		newCls = assignPoints(Cents, oldCls, k)
		if oldCls == newCls:
			run = False
		oldCls = newCls
	for i in range(len(allPoints)):
		print allPoints[i] , ' is in ', newCls[i], '\n'
	print 'Centroids are: ', Cents

KMeans(3)
