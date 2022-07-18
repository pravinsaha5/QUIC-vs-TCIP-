# -*- coding: utf-8 -*-
"""
This script takes the output of comparision.py to extract only the data required (timestamp and bytes).
"""

import os
from os import listdir
from os.path import isfile, join

import collections
import re


def converttosec(time):
	seconds = 0
	temp = time[2].split('.')
	seconds = 60 * float(time[1]) + float(temp[0]) + \
		(0.5 if int(temp[1]) >= 500000 else 0)
	if seconds < 0:
		seconds = 0.0
	return seconds

# key of dictionary will be time and value be number of packets
# this function will store the time and number of packets of that time in dictionary
def initializeDict(dic, time, pcks):
	if dic.has_key(time):
		dic[time] += pcks
	else:
		dic[time] = pcks
	return


openpath = os.path.normpath('./raw')
savepath = os.path.normpath('./processed')
onlyfiles = [os.path.normpath(openpath + '/' + f)
			 for f in listdir(openpath) if isfile(join(openpath, f))]
onlyfilessave = [savepath + '/' +
				 f for f in listdir(openpath) if isfile(join(openpath, f))]


for file in onlyfiles:
	average_bandwidth = 0
	total_overhead = -32000000
	initial_time = 0
	final_time = 0
	bytesps = collections.OrderedDict()
	print "Processing file: " + file
	with open(file, 'r') as f:
		l = f.readline()
		div = l.split()
		time = div[0].split(':')
		time2 = time[2].split('.')
		initial_time = float(time2[0]) + float(float(time2[1]) / 1000000)
		actual_second = converttosec(time)

		initializeDict(bytesps, float(actual_second), int(
			re.search(r'\d+', div[-1]).group()))
		total_overhead += bytesps[actual_second]
		f.next()
		last_actual = actual_second
		for line in f:
			try:
				div = line.split()
				time = div[0].split(':')
			except:
				continue
			try:
				actual_second = converttosec(time)
			except:
				actual_second = last_actual
			last_actual = actual_second
			if div[-1] == "[|ether]":
				continue
			try:
				pckbytes = int(re.search(r'\d+', div[-1]).group())
			except:
				print div
			initializeDict(bytesps, float(actual_second), pckbytes)
			total_overhead += pckbytes
			try:
				next(f)
			except:
				break

	temp = time[2].split('.')
	final_time = float(time[1]) * 60 + float(temp[0]
											   ) + float(float(temp[1]) / 1000000)
	savePath = os.path.normpath(file.replace(
		openpath + '/', savepath + '/SUM'))
	filePath = open(savePath + '.txt', 'w')

	for key in sorted(bytesps.keys()):
		filePath.write(str(key) + ' ' + str(bytesps[key]) + '\n')
		average_bandwidth += float(bytesps[key] * 2)

	average_bandwidth = float(average_bandwidth / len(bytesps.keys()))
	filePath.close()
	savePath = os.path.normpath(file.replace(
		openpath + '/', savepath + '/DATA'))
	filePath = open(savePath + '.txt', 'w')
	filePath.write(str(total_overhead) + ' ' + str(initial_time) +
				  ' ' + str(final_time) + ' ' + str(average_bandwidth))
	filePath.close()
