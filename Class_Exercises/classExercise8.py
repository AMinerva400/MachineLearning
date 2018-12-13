#!/usr/bin/python
#Author: Anthony Minerva
#Date: October 17th, 2018
#Desc: Class Exercise 8 - Calculating Covariance Matrix

def calcMean(X):
	sumX = 0.0
	for i in range(len(X)):
		sumX += X[i]
	sumX = sumX / len(X)
	return sumX	

def calcAdjusted(X):
	AdjX = X
	meanX = calcMean(X)
	for i in range(len(X)):
		AdjX[i] -= meanX
	return AdjX

def calcCovariance(X, Y):
	n = len(X)
	AdjX = calcAdjusted(X)
	AdjY = calcAdjusted(Y)
	total = 0.0
	for i in range(len(AdjX)):
		total += AdjX[i] * AdjY[i]
	total = total / (n - 1)
	return total

def calc2DMatrix(X, Y):
	dimens = 2
	vals = [X, Y]
	matrix = [[0, 0], [0, 0]]
	for i in range(dimens):
		for j in range(dimens):
			matrix[i][j] = calcCovariance(vals[i], vals[j])
	return matrix

def calc3DMatrix(X, Y, Z):
	dimens = 3
	vals = [X, Y, Z]
	matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	for i in range(dimens):
		for j in range(dimens):
			matrix[i][j] = calcCovariance(vals[i], vals[j])
	return matrix

def main():
	X = [1.0, -1.0, 4.0]
	Y = [2.0, 1.0, 3.0]
	Z = [1.0, 3.0, -1.0]
	#print calc2DMatrix(X, Y)
	print calc3DMatrix(X, Y, Z)

main()
