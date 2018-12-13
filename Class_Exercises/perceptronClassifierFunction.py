# MCP Neuron and Perceptron Model
# Prof. Steven C. Lindo
# Chapter 2 - Perceptrons
# Sept 2017

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from mcpperceptron import Perceptron
from matplotlib.colors import ListedColormap

# Function to plot the decision boundary based on the
# results from the perceptron classifier
def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, Z, alpha = 0.4, cmap = cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x = X[y == cl, 0], y = X[ y == cl, 1],
                    alpha = 0.8, c = cmap( idx),
                    marker = markers[idx], label = cl)

# First lets read in the iris data sets into a
# pandas data frame called df        
def read_file():    
    csv_file = "irisdata.csv"
    df = pd.read_csv(csv_file)
    print(df.info())
    print(df.head())

    return df

# Next extract the first 100 class labels that
# correspond to the 50 Iris-Setosa and 50
# Iris-Versicolor flowers, respectively, and
# convert the class labels into the two integer
# class labels y and X
def extract_classes(df):

    # get the first 100 in the data sets.
    y = df.iloc[0:100,4].values

    # if setosa label = -1, else label = 1
    y = np.where(y == 'Iris-setosa', -1, 1)

    # get the feature coordinates
    # 0 index in the data frame is sepal_length
    # 0 1 is not linearly separable
    # 2 index in the data frame is petal_length
    X = df.iloc[0:100,[0,2]].values

    # Use matplotlib to plot visualize in
    # a two dimension scatter plot
    plt.scatter(X[:50, 0], X[:50, 1],color ='red', marker ='o', label ='setosa')
    plt.scatter(X[50:100, 0], X[50:100, 1], color ='blue', marker ='x', label ='versicolor')

    plt.xlabel('sepal length')
    plt.ylabel('petal length')
    plt.legend( loc ='upper left')

    plt.show()

    return X, y

# - - - main program - - - #

# read the iris data file into a dataframe
irisDF = read_file()

# Extract the features and class labels
X, y   = extract_classes(irisDF)

# Next,train our perceptron algorithm on the
# Iris data subset that we just extracted
ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)

# Plot the results in a line chart 
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker ='o') 
plt.xlabel('Epochs') 
plt.ylabel('Number of misclassifications') 
plt.show()

# Next, train and classify the decision boundary
plot_decision_regions( X, y, classifier = ppn) 
plt.xlabel(' sepal length [cm]') 
plt.ylabel(' petal length [cm]') 
plt.legend( loc ='upper left') 
plt.show()

p = ppn.predict([[5.1, 3.2], [4.2,3.3]])
print('\nPredictions = ',p)

# - - - end main program - - - #


