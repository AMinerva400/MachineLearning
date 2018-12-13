# Dr. Steven C. Lindo
# Nov 2018
# Perceptron Neural Network

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from mcpperceptron import Perceptron
from matplotlib.colors import ListedColormap

def plotData(df, y):
    y = np.where(y == 'Iris-setosa', -1, 1)
    X = df.iloc[0:100, [1, 3]].values

    plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
    plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')

    plt.xlabel('Epochs')
    plt.ylabel('Number of Classifications')

    plt.legend(loc='upper left')
    
    plt.show()

def trainPerceptron(df):
    ppn = Perceptron(eta=0.1, n_iter=10)
    X = df.iloc[0:100, 0].values
    y = df.iloc[0:100, 2].values
    ppn.fit(X, y)
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.show()
    p = ppn.predict([[1,2], [4,1]])
    print("\nPredictions: ", p)
    
                                      
def main():
    # Load the iris data in a pandas dataframe
    print("\nLoading Iris data set ..\n")

    df = pd.read_csv('irisdata.csv')
    print(df.tail())
    y = df.iloc[0:100, 4].values
    plotData(df, y)
    trainPerceptron(df)    

main()

