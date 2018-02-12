import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import sys
from matplotlib.ticker import ScalarFormatter
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})  #used for fiting the subplot
rcParams.update({'xtick.labelsize':10})
rcParams.update({'ytick.labelsize':10})

def readFile(filePath):

	f=open(filePath)
	x=[]
	for line in f:
		val=float(line.strip('\n'))
		if val>0.009:
			x+=val,

	return x

# def y_fmt(x, y):
#     return '{:2.2e}'.format(x).replace('e', 'x10^')



if __name__=="__main__":
	#degree distribution 
	folder="/Users/dongqingxiao/Documents/uncertainGraphProject/allDataSet/input/"
	
	xlabel_='Edge-Probability'
	dataset=['dblp','bright','ppi']
	fig, axs = plt.subplots(1,3,figsize=(9,3))
	for i in xrange(3):
		data=dataset[i]
		x=readFile(folder+data+"_p_e.txt")
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
		ax.set_xlim([0,1])
	plt.show()


	
	



