#!/usr/bin/python
#Author : Anthony Minerva
#Date : September 12th, 2018
#Desc : Class Exercise 2 : City Distance

def distance(x1, y1, x2, y2):
	dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
	return float("{0:.2f}".format(dist))

cityX = [-1, -1, 1, 2, 2, 3, 4, 4]
cityY = [3, -1, 1, 0.5, -1, 3, 2, -0.5]

cityDistance = [
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0]
]

for i in range(len(cityX)):
	for j in range(len(cityY)):
		cityDistance[i][j] = distance(cityX[i], cityY[i], cityX[j], cityY[j])

for i in range(len(cityDistance)):
	print cityDistance[i]


