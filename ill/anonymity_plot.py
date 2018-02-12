import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})


def readDataset(filpath):
	f=open(filpath)
	x=[]
	y=[]
	l=0 
	for line in f:
		if l%2==0:
			line=line.rstrip()
			lines=line.split('\t')
			x+=int(lines[0]),
			y+=int(lines[1]),
		l+=1

	return x, y 


def semiPlot(ax,x,y,c,m,le,fill='None'):
	ax.plot(x,y,marker=m,linestyle='None',label=le,markersize=6,markerfacecolor=fill,markeredgecolor=c)
	ax.locator_params(axis='y',nbins=4)
	ax.locator_params(axis='x',nbins=5)


dblp_x,dblp_y=readDataset('./dblp_an.txt')
dblp_x_rep,dblp_y_rep=readDataset('./dblp_rep.txt')
ppi_x,ppi_y=readDataset('./ppi_an.txt')
ppi_x_rep,ppi_y_rep=readDataset('./ppi_rep.txt')
fig, axs = plt.subplots(1,1,figsize=(4,3))
semiPlot(axs,dblp_x,dblp_y,'r','o','DBLP',fill='r')
plt.hold(True)
semiPlot(axs,dblp_x_rep,dblp_y_rep,'k','>','DBLP-rep',fill='k')
plt.title('DBLP',fontsize=12)
plt.axis([0,300,0,2000])




plt.legend(loc=2,numpoints=1,fontsize=10,ncol=1)
plt.xlabel('k',fontsize=14)
plt.ylabel('Number of nodes',fontsize=14)

plt.show()
