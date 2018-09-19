# IrisFlower.py

'''
THE IRIS DATASET

The Iris dataset is a classic dataset from the 1930s; it is one of the first modern
examples of statistical classification.
'''

__author__ = 'Le Quang Vinh'
__version__ = '1.0.0'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def main():
	
	data = load_iris()
	features = data['data']
	feature_names = data['feature_names']
	target = data['target']

	print(feature_names)
	''' Visualize data with sepal length and width
	The sepal length and width seem to be able to seperate Iris Setosa
	'''
	for t, marker, c in zip(np.arange(3), '>ox', 'rgb'):
		plt.scatter(features[target == t,0],
					features[target == t,1],
					marker = marker,
					c = c)
	plt.xlabel(feature_names[0])
	plt.ylabel(feature_names[1])
	plt.show()
	return

if __name__ == '__main__':
	main()