# MetaTrader.py

import sys, re, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def CollectData(filename):
	data = pd.read_csv(filename, header=0, sep=';')
	return data

def SmoothData(data, N):
	cumsum, moving_aves = [0], []

	for i, x in enumerate(data, 1):
		cumsum.append(cumsum[i-1] + x)
		if i>=N:
			moving_ave = (cumsum[i] - cumsum[i-N])/N
			moving_aves.append(moving_ave)

	return moving_aves

def GraphPrice(time, price_data, ratio=""):
	f, axarr = plt.subplots(2, 1, sharex=True)
	f.canvas.set_window_title("Relationship between EUR and USD")

	x = [datetime.strptime(time_string, "%Y.%m.%d") for time_string in time]

	SMA_34 = price_data.rolling(window=34).mean()
	SMA_34.tail()

	axarr[0].set_title("Price relationship", loc='left')
	axarr[0].set(ylabel="EUR/USD", ylim=(price_data.min()*0.95, price_data.max()*1.05))
	axarr[0].plot(x, price_data, c='g', linewidth=1)
	axarr[1].set_title("Moving Average", loc='left')
	axarr[1].set(xlabel="Date/Time", ylabel="SMA", ylim=(price_data.min()*0.95, price_data.max()*1.05))
	axarr[1].plot(x, SMA_34, c='r', linewidth=1)
	return

def main():
	data = CollectData('EURUSD.csv')

	summary = data.describe()
	print(summary)
	print('\n\n')
	print(data.head())

	time = data.iloc[-100:, 0]
	close_prices = data.iloc[-100:, 4]

	GraphPrice(time, close_prices, "EUR/USD")
	plt.show()

	return

if __name__ == '__main__':
	main()