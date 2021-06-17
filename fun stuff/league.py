import math
import sys
import statistics
import argparse
basearm = 20
armor = 40
totalarmor = basearm+armor
import csv
with open('items.csv', newline='') as itemcsv:
	csv_reader = csv.reader(itemcsv)
	
	for line in csv_reader:
		words = []
		words.append(line[0])
		names = ''.join(words)
		print(names)
		ad1 = []
		ad1.append(line[1])
		ad = ''.join(ad1)
		print(ad1)

