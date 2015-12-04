# -*- conding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math
import urllib2

def main():
	# config
	fig = plt.figure(facecolor="white")
	ax = fig.add_subplot(111)
	ax.set_title("Matsuyama, Ehime")
	ax.set_xlabel("Year / y")
	ax.set_ylabel("Temperature / C^")
	legend = []
	for i in range(13):
		if i == 12:
			legend.append("Average")
		else:
			legend.append(str(i+1))

	colors = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78',
			'#2ca02c', '#98df8a', '#d62728', '#ff9896',
			'#9467bd', '#c5b0d5', '#8c564b', '#c49c94',
			'#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7',
			'#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

	# set file name
	data = read_data("data")

	x,y = [],[]
	for i in range(len(data)):
		x.append(data[i][0])
		data[i].pop(0)
		y.append(data[i])

	for j in range(13):
		y_temp = []
		for i in range(len(data)):
			y_temp.append(y[i][j])
		ax.plot(x, y_temp, color=colors[j])
		plt.text(2020.5, y_temp[-1], legend[j], fontsize=12, color=colors[j])
	
	plt.show()

#read file and make data array
def read_data(d):
	data = []
	for i,line in enumerate(open(d, "r")):
		if i == 0:
			pass
		elif i % 2:
			year = (line.rstrip()+"\t")
		else:
			try:
				data.append(map(float, (year+line).rstrip('\n[]() ').split('\t')))
			except:
				pass
	return data

main()
