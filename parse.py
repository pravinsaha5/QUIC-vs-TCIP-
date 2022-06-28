# -*- coding: utf-8 -*-
"""
This script takes the output of script.py from the openPath folder, and processes
the files in order to extract only the data required (timestamp and bytes).
Output files saved to /processed
This script should be run after script.py
"""

import os
from os import listdir
from os.path import isfile, join

import collections
import re


def converttosec(time1):
	seconds = 0
	temp = time1[2].split('.')
	seconds = 60 * float(time1[1]) + float(temp[0]) + \
		(0.5 if int(temp[1]) >= 500000 else 0)
	if seconds < 0:
		seconds = 0.0
	return seconds


def actualizedict(dic, time1, pcks):
	if time1 in dic.keys():
		dic[time1] += pcks
	else:
		temp = time1 - 0.5
		while (not temp in dic.keys()) and temp >= 0:
			dic[temp] = 0
			temp -= 0.5
		dic[time1] = pcks
	return


openpath = os.path.normpath('F:\new_ACN\new_ACN')
savepath = os.path.normpath('F:\new_ACN\new_processed')
onlyfiles = [os.path.normpath(openpath + '/' + f)
			 for f in listdir(openpath) if isfile(join(openpath, f))]
onlyfilessave = [savepath + '/' +
				 f for f in listdir(openpath) if isfile(join(openpath, f))]


for fich in onlyfiles:
	throughput = 0
	total_overhead = -32000000
	initial_time = 0
	final_time = 0
	bytesps = collections.OrderedDict()
	print("Processing file: " + fich)
	with open(fich, 'r') as f:
		l = f.readline()
		div = l.split()
		
		time1 = div[0].split(':')
		time2 = time1[2].split('.')
		initial_time = float(time2[0]) + float(float(time2[1]) / 1000000)
		actual_second = converttosec(time1)

		actualizedict(bytesps, float(actual_second), int(
			re.search(r'\d+', div[-1]).group()))
		total_overhead += bytesps[actual_second]
		f.next()
		last_actual = actual_second
		for line in f:
			try:
				div = line.split()
				time1 = div[0].split(':')
			except:
				continue
			try:
				actual_second = converttosec(time1)
			except:
				actual_second = last_actual
			last_actual = actual_second
			if div[-1] == "[|ether]":
				continue
			try:
				pckbytes = int(re.search(r'\d+', div[-1]).group())
			except:
				print(div)
			actualizedict(bytesps, float(actual_second), pckbytes)
			total_overhead += pckbytes
			try:
				next(f)
			except:
				break

	temp = time1[2].split('.')
	final_time = float(time1[1]) * 60 + float(temp[0]
											   ) + float(float(temp[1]) / 1000000)


	for key in sorted(bytesps.keys()):
		file.write(str(key) + ' ' + str(bytesps[key]) + '\n')
		throughput += float(bytesps[key] * 2)
		
	### contribution - averaging the throughput and adding it in the parsed file ###
	avg_throughput = float(throughput / len(bytesps.keys()))
	
	file.close()
	rutasave = os.path.normpath(fich.replace(
		openpath + '/', savepath + '/DATA'))
	file = open(rutasave + '.txt', 'w')
	file.write(str(total_overhead) + ' ' + str(initial_time) +
				  ' ' + str(final_time) + ' ' + str(avg_throughput))
	file.close()