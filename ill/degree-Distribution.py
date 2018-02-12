import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import sys
from matplotlib.ticker import ScalarFormatter
from matplotlib import rcParams
from collections import defaultdict 
rcParams.update({'figure.autolayout': True})  #used for fiting the subplot


def readFile(filePath):

	f=open(filePath)
	x=[]
	x_range=defaultdict(int)
	for line in f:
		val=float(line.strip('\n'))
		if val>0.009:
			x+=val,
		x_index=int(val/5)
		x_range[x_index]+=1

	x_len=len(x)
	x=filter(lambda item: x_range[int(item/5)]<60, x)
	frac=float(len(x))/x_len

	return x,frac

# def y_fmt(x, y):
#     return '{:2.2e}'.format(x).replace('e', 'x10^')



if __name__=="__main__":
	#degree distribution 
	folder="/Users/dongqingxiao/Documents/uncertainGraphProject/allDataSet/degreeSequence/"
	# data=sys.argv[1]
	xlabel_='Degree'

	dataset=['dblp','bright','ppi']
	fracs=[0.0004,0.005,0.07]
	fig, axs = plt.subplots(1,3,figsize=(9,3))

	for i in xrange(3):
		data=dataset[i]
		filepathpath="{}{}/{}.txt".format(folder,data,data)
		x,frac=readFile(filepathpath)
		ax=axs[i]
		ax.hist(x,bins=100)
		y_formatter=ScalarFormatter(useMathText=True)
		y_formatter.set_powerlimits((5,5))
		ax.yaxis.set_major_formatter(y_formatter)
		ax.set_ylabel('Frequency',fontsize=14)
		ax.set_xlabel(xlabel_,fontsize=14)
		if data=='bright':
			data="Brightkite"
		ax.set_title(data.upper(),fontsize=14)
		ax.locator_params(axis='x',nbins=5)
		ax.locator_params(axis='y',nbins=4)
		# ax.tick_params(axis='both', which='major', labelsize=6)
		ax.annotate(str(round(frac,4)),xy=(0.5,0.7),xycoords='axes fraction',fontsize=20)
	plt.show()



