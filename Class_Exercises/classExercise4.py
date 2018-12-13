#!/usr/bin/python
#Author: Anthony Minerva
#Date: September 17th, 2018
#Desc: Class Exercise 4: Linear Regression

from pandas import DataFrame

def estimateLine(xValues, yValues):
	xMean = calcMean(xValues)
	yMean = calcMean(yValues)
	xDiff = calcXDiff(xValues, xMean)
	yDiff = calcYDiff(yValues, yMean)
	xDiff2 = calcXDiff2(xDiff)
	xyDiff = calcXYDiff(xDiff, yDiff)
	b1 = calcB1(xDiff2, xyDiff)
	b0 = calcB0(xMean, yMean, b1)
	yHat = [0] * len(yValues)
	for i in range(len(yValues)):
		yHat[i] = estimateValue(xValues[i], b1, b0)
	ds = makeDataSet(xValues, yValues, xDiff, yDiff, xDiff2, xyDiff, yHat)
	df = makeDataFrame(ds)
	R2 = calcR2(yValues, yMean)
	SE = calcSE(yValues, yHat)
	print df.head()
	print 'X-Mean = ' + str(xMean) + ' Y-Mean = ' + str(yMean)
	print 'B1 = ' + str(b1)
	print 'B0 = ' + str(b0)
	print 'R^2 = ' + str(R2)
	print 'Standard Error = ' + str(SE)

def calcMean(xValues):
	return sum(xValues) / len(xValues)

def calcXDiff(xValues, xMean):
	xDiff = [0] * len(xValues)
	for i in range(len(xDiff)):
		xDiff[i] = xValues[i] - xMean
	return xDiff

def calcYDiff(yValues, yMean):
	yDiff = [0] * len(yValues)
	for i in range(len(yDiff)):
		yDiff[i] = yValues[i] - yMean
	return yDiff

def calcXDiff2(xDiff):
	xDiff2 = [0] * len(xDiff)
	for  i in range(len(xDiff2)):
		xDiff2[i] = xDiff[i]**2
	return xDiff2

def calcXYDiff(yDiff, xDiff):
	xyDiff = [0] * len(yDiff)
	for i in range(len(xyDiff)):
		xyDiff[i] = xDiff[i] * yDiff[i]
	return xyDiff

def calcB1(xDiff2, xyDiff):
	sumX = 0.0
	sumY = 0.0
	for i in range(len(xDiff2)):
		sumX += xDiff2[i]
		sumY += xyDiff[i]
	return sumY / sumX		

def calcB0(xMean, yMean, b1):
	return yMean - (xMean * b1)

def calcR2(yValues, yMean):
	total = 0
	for i in range(len(yValues)):
		total = total + (yValues[i] - yMean)**2
	return (total / (len(yValues) - 1))**0.5

def calcSE(yValues, yEst):
	total = 0
	for i in range(len(yValues)):
		total = total + (yValues[i] - yEst[i])**2
	return (total / (len(yValues) - 1))**0.5

def estimateValue(x, b1, b0):
	return b0 + (b1 * x)

#x y xidff ydiff xdiff2 ydiffxdiff label: yEst
def makeDataSet(f1, f2, f3, f4, f5, f6, l1):
        dataSet = list(zip(f1, f2, f3, f4, f5, f6, l1))
        return dataSet

def makeDataFrame(ds):
        dataFrame = DataFrame(ds, columns = ['X', 'Y', 'X - XMean', 'Y - YMean', '(X - XMean)^2', '(X - XMean) * (Y - YMean)', 'Estimated Y Values'])
        return dataFrame
	
x1 = [1.0, 2.0, 3.0, 4.0, 5.0]
y1 = [3.0, 5.0, 7.0, 5.0, 6.0]
x2 = [1.0, 2.0, 3.0 ,4.0, 5.0]
y2 = [1.0, 3.0, 3.0, 2.0, 6.0]
estimateLine(x1,y1)
estimateLine(x2,y2)
