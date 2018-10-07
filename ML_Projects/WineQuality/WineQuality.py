__author__ = 'Le Quang Vinh'
__version__ = '1.0.0'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def CollectData(filename):
	data = pd.read_csv(filename, header=0, sep=';')
	return data

def main():
	data = CollectData('winequality-red.csv')

	# Statistical summaries
	print('DATASET SUMMARY')
	summary = data.describe()
	print(summary)
	print('\n\n')

	return

if __name__ == '__main__':
	main()