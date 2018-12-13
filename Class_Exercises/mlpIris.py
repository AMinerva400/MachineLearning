# Dr. Steven C. Lindo
# MLP with IRIS data

import pandas as pd
import numpy as np

from sklearn.neural_network import MLPClassifier

def numToTextLabels(y):
	y_text = np.where(y == -1, 'Iris-setosa', 'Iris-virgina')
	return y_text	

def main():

	df = pd.read_csv('irisdata.csv')
	print(df.head())

	# setosa and versicolor
	y = df.iloc[0:100, 4].values
	y = np.where(y == 'Iris-setosa', -1, 1)

	# sepal length and petal length
	X = df.iloc[0:100, [0,2]].values
	#Can change adam to sgd 
	clf = MLPClassifier(activation='relu', learning_rate_init=0.01, solver='adam', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1, verbose=True)

	clf.fit(X,y)

	p = clf.predict(([ [3.2,2], [5.3, 2.1] ]))

	print '\nPredicted :', numToTextLabels(p)

	print '\nClf Object\n', clf


# - - - - -  Run main  - - - -  
main()
