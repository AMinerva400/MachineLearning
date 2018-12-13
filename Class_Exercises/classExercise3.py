#!/usr/bin/python
#Author : Anthony Minerva 
#Date : September 12th, 2018
#Desc : Class Exercise 3: Working with Pandas

from pandas import DataFrame, read_csv
import pandas as pd

def makeDataSet(f1, f2, f3, l1):
	dataSet = list(zip(f1, f2, f3, l1))
	return dataSet

def makeDataFrame(ds):
	dataFrame = DataFrame(ds, columns = ['Names', 'Height', 'Weight', 'Dunk'])
	return dataFrame

def main():
	#ds = makeDataSet(names, height, weight, dunk)
	#df = makeDataFrame(ds)
	#print df.info()
	#print df.head()

	df = pd.read_csv("schoolgrants.csv")
	isNY = df['State'] == "NY"
	isNJ = df['State'] == "NJ"
	isCT = df['State'] == "CT"
	df['AwardAmount'] = df['AwardAmount'].str.slice(1)
	totalNYAwards = pd.to_numeric(df['AwardAmount'][isNY]).sum()
	totalNJAwards = pd.to_numeric(df['AwardAmount'][isNJ]).sum()
	totalCTAwards = pd.to_numeric(df['AwardAmount'][isCT]).sum()
	NYMean = pd.to_numeric(df['AwardAmount'][isNY]).mean()
	NJMean = pd.to_numeric(df['AwardAmount'][isNJ]).mean()
	CTMean = pd.to_numeric(df['AwardAmount'][isCT]).mean()
	NYMedian = pd.to_numeric(df['AwardAmount'][isNY]).median()
        NJMedian = pd.to_numeric(df['AwardAmount'][isNJ]).median()
        CTMedian = pd.to_numeric(df['AwardAmount'][isCT]).median()
	NYSTD = pd.to_numeric(df['AwardAmount'][isNY]).std()
        NJSTD = pd.to_numeric(df['AwardAmount'][isNJ]).std()
        CTSTD = pd.to_numeric(df['AwardAmount'][isCT]).std()
	print df[['School Name', 'AwardAmount', 'State']][isNY | isNJ | isCT]
	print "Total Award Amount for State NY = " + str(totalNYAwards)
	print "Mean for State NY = " + str(NYMean)	
	print "Median for State NY = " + str(NYMedian)
	print "Standard Deviation for State NY = " + str(NYSTD)
	print "Total Award Amount for State NJ = " + str(totalNJAwards)
	print "Mean for State NJ = " + str(NJMean)
	print "Median for State NJ = " + str(NJMedian)
	print "Standard Deviation for State NJ = " + str(NJSTD)
	print "Total Award Amount for State CT = " + str(totalCTAwards)
	print "Mean for State CT = " + str(CTMean)
	print "Median for State CT = " + str(CTMedian)
	print "Standard Deviation for State NJ = " + str(CTSTD)	



#names = ['Peter', 'John', 'Beatrice', 'Maxx', 'Jeanine']
#height = [83, 74, 65, 68, 81]
#weight = [276, 201, 159, 145, 198]
#dunk = ['Yes', 'Yes', 'Yes', 'No', 'No']


main()
