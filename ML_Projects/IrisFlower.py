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

def VisualizationData(data):
	features = data['data']
	feature_names = data['feature_names']
	target = data['target']

	f, axarr = plt.subplots(2, 3)
	f.canvas.set_window_title('IrisFlower Plants Database')
	f.suptitle('Iris flower classification based on length and width of sepal and petal')

	# Visualize data
	pos = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]
	x_col = [0, 0, 0, 1, 1, 2]
	y_col = [1, 2, 3, 2, 3, 3]
	for p, x, y in zip(pos, x_col, y_col):
		for t, marker, c in zip(np.arange(3), '>ox', 'rgb'):
			axarr[p].scatter(features[target == t, x],
								features[target == t, y],
								marker = marker,
								c = c)
			axarr[p].set(xlabel = feature_names[x], ylabel = feature_names[y])

	plt.show()
	return

def main():
	
	data = load_iris()
	VisualizationData(data)
	return

if __name__ == '__main__':
	main()