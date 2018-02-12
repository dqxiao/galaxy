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
		# if val>0.0009:
		x+=val,

	# x_min=min(x)
	# x_max=max(x)
	# diff=x_max-x_min
	# x=[(item-x_min)/diff for item in x]
	# len=
	# x=filter(lambda item: item>0.2,x)
	return x


# def y_fmt(x, y):
#     return '{:2.2e}'.format(x).replace('e', 'x10^')



if __name__=="__main__":
	#degree distribution 
	folder="/Users/dongqingxiao/Documents/uncertainGraphProject/allDataSet/relOutput/"
	
	xlabel_='Reliability Centrality'
	dataset=['dblp']
	fig, ax = plt.subplots(figsize=(5,4))
	for i in xrange(1):
		data=dataset[i]
		filePath="{}{}/{}".format(folder,data,"reliablityNode/nodeRelDiff_E.txt")
		x=readFile(filePath)
		# ax=axs[i]
		ax.hist(x,bins=50)
		#ax.boxplot(x,0,'rs',0,0.1)
		y_formatter=ScalarFormatter(useMathText=True)
		x_formatter=ScalarFormatter(useMathText=True)
		x_formatter.set_powerlimits((5,5))
		ax.yaxis.set_major_formatter(y_formatter)
		ax.xaxis.set_major_formatter(x_formatter)
		ax.set_ylabel('# of nodes',fontsize=14)
		ax.set_xlabel(xlabel_,fontsize=14)
		if data=='bright':
			data="Brightkite"
		ax.set_title(data.upper(),fontsize=12)
		ax.locator_params(axis='x',nbins=3)
		ax.locator_params(axis='y',nbins=4)
		x_max=max(x)
		plt.yscale('log')
		#ax.set_xlim([0,x_max])
		
	plt.show()


	
	



