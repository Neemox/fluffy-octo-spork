##peakFinder.py
## The goal of this program is to take a paired list of values, find the maximum values within one fo the data sets, and return the paired value from the other data set.


## this is a major work in progress, but will be useful for finding maximum peaks in deconvoluted mass spectra,
import csv
with open('filename.csv', newline='') as csvfile:
		chromatogram = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in chromatogram:
			print(', '.join(row))
		highValue = max(chromatogram)
		print(highValue)
