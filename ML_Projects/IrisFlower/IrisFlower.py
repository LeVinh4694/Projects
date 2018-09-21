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

def AnalyzeData(data):
	features = data['data']
	labels = data['target']

	plength = data['data'][:,2]
	is_setosa = (labels == 0)
	max_setosa = plength[is_setosa].max()
	min_non_setosa = plength[~is_setosa].min()
	print('Classify setosa')
	print('  - Maximum of setosa: {0}(cm).'.format(max_setosa))
	print('  - Minimum of others: {0}(cm).'.format(min_non_setosa))

	# Analyze non setosa features
	features = features[~is_setosa]
	labels = labels[~is_setosa]

	is_virginica = (labels == 2)
	best_acc = -1.0
	for fi in range(features.shape[1]):
		# Generate all possible threshold for current feature
		thresh = features[:,fi].copy()
		thresh.sort()
		# Test all threshold
		for t in thresh:
			pred = (features[:,fi] > t)
			acc = (pred == is_virginica).mean()
			if acc > best_acc:
				best_acc = acc
				best_fi = fi
				best_t = t
	print('\nClassify Virginica and Versicolor (feature > threshold => Virginica)')
	print('  - The best accuracy is: {0}%'.format(int(best_acc*100)))
	print('  - Feature column: {0}'.format(best_fi))
	print('  - Threshold: {0}'.format(best_t))

	return

def PredictModel(feature):
	threshold = 1.6

	if feature[2] < 2.0:
		print('Iris Setosa.')
	else:
		if feature[3] > threshold:
			print('Iris Verginica.')
		else:
			print('Iris Versicolor.')
	return

def VisualizeData(data):
	features = data['data']
	feature_names = data['feature_names']
	target = data['target']

	f, axarr = plt.subplots(2, 3)
	f.canvas.set_window_title('IrisFlower Plants Database')
	f.suptitle('Iris flower classification based on length and width of sepal and petal')

	# Scatter data
	pos = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]
	col = [[0, 0, 0, 1, 1, 2], [1, 2, 3, 2, 3, 3]]
	for p, x, y in zip(pos, col[0], col[1]):
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
	
	print(data['DESCR'])

	#AnalyzeData(data)

	PredictModel(data['data'][0])
	PredictModel(data['data'][50])
	PredictModel(data['data'][100])

	#VisualizeData(data)
	return

if __name__ == '__main__':
	main()