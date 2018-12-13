#!/usr/bin/python
#Author: Anthony Minerva
#Date: October 22nd, 2018
#Desc: Calculating Eigens - Class Example

import numpy as np

def calcEigen(A):
	eig_value, eig_vector = np.linalg.eig(A)
	#for x in range(len(eig_value)):
		#print 'Eigen Values: ', eig_value[x]
		#print 'Eigen Vectors: ', eig_vector[x]
	return eig_value, eig_vector

def main():
	A = np.array( [
	[6, 6, 2, 3],
	[5, 6, 1, 2],
	[4, 1, 2, 1],
	[5, 4, 2, 1]
	] )
	#Calculate Covariance of the Matrix
	cov_A = np.cov(A)
	w, v = calcEigen(cov_A)
	#Create Eigen Pairs of Vectors and Values
	eig_pairs = [(np.abs(w[i]), v[:,i]) for i in range(len(w))]
	#Sort the Eigen Pairs
	eig_pairs.sort()
	eig_pairs.reverse()
	print '\nEigenvectors\n', eig_pairs
	print '\nThe sorted Eigen Values:'
	for i in eig_pairs:
		print i[0]
main()
