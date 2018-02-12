import matplotlib.pyplot as plt 
import numpy as np
import math
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
# from mpl_toolkits.mplot3d import Axes3D

# import plotly.tools as tls
# tls.set_credentials_file(username='dqxiao', api_key='nrxt9u7vmn')




from matplotlib.ticker import OldScalarFormatter,ScalarFormatter

def readFile(filePath):

	f=file(filePath)
	Y=[]
	for line in f:

		# lines=line.strip().split('\t')
		Y.append(float(line))

	#Y.sort()
	return np.asarray(Y)
	#return Y 


def scale(data):

	datasum=sum(data)

	data/=datasum

	return np.asarray(data)



def dataProcess(choice, xuniq, dx, maxX):


	# values=[0]*(int(maxX/dx)+1)
	values=dict()
	count=[0]*(int(maxX/dx)+1)
	


	length=len(choice)

	for i in range(int(maxX/dx)+1):
		values[i]=[]


	for i in range(length):

		val=int((xuniq[i]-0.5*dx)/dx)
		values[val].append(choice[i])

		count[val]+=1

	data=[values[val] for val in values]

	#print count

	pos=[]
	xticks=[]
	for val in values:
		pos.append(val+1)
		xticks.append((val+0.5)*dx)

	return data, pos, xticks,count

def splitData(uniq,sen,choiceChange, torleance):

	length=len(uniq)


	# dataAll=[uniq,sen, choiceChange]

	# dataAll=np.asarray(dataAll)
	# dataAll=np.asarray()
	

	uniq_pos=[]
	sen_pos=[]
	choice_pos=[]

	uniq_neg=[]
	sen_neg=[]
	choice_neg=[]


	for i in xrange(length):

		if choiceChange[i]> torleance:
			uniq_pos.append(uniq[i])
			sen_pos.append(sen[i])
			choice_pos.append(choiceChange[i])
		if choiceChange[i]< -1*torleance:
			uniq_neg.append(uniq[i])
			sen_neg.append(sen[i])
			choice_neg.append(choiceChange[i])
	
	data=[uniq_pos, sen_pos, choice_pos,uniq_neg, sen_neg, choice_neg]

	return data



# boxplot 
def plotTest(ax,random_choice,uniq, dx, maxX):

	cd,pos,xticks,count=dataProcess(random_choice,uniq, dx, maxX)

	formatter = ScalarFormatter(useMathText=True)
	formatter.set_powerlimits((6,6))
	ax.yaxis.set_major_formatter(formatter)
	ax.boxplot(cd,0,'')
	# ax.set_ylim(-0.0005,0.006)
	# ax.set_ylim(-0.0005,0.015)
	ax.locator_params(axis='y',nbins=5)
	ax.xaxis.set_ticks(pos,xticks)





	pos_new=[]
	xticks_new=[]

	indice=xrange(0,len(pos),2)

	pos_new=[pos[i] for i in indice]
	xticks_new=[xticks[i] for i in indice]

	return [pos_new,xticks_new, count,pos]



def filterVector(uniq,sen,choice,filePath,c):

	f=open(filePath,'w')

	length=len(uniq)
	for i in range(length):
		if choice[i]>c or uniq[i]>0.5 or sen[i]>0.5:
			s="{},{},{}\n".format(uniq[i],sen[i],choice[i])
			f.write(s)

	f.close()


def justFilter(uniq,sen,choice,c):
	uniqF=[]
	senF=[]
	choiceF=[]

	length=len(uniq)
	for i in range(length):
		if uniq[i]>0.2 or sen[i]>0.5 :
			uniqF.append(uniq[i])
			senF.append(sen[i])
			choiceF.append(choice[i])

	return (uniqF,senF,choiceF)


def roundup(x):
	return int(math.ceil(x / 100.0)) * 100



def choicePlot():



	# folder="/Users/dongqingxiao/Documents/uncetainGraphProject/allDataSet/progTest/hepth/"
	folder="/Users/dongqingxiao/Documents/uncertainGraphProject/allDataSet/progTest/vectorlog/"

	cF="random_nodeChoice.txt"
	cgF="greedy_nodeChoice.txt"

	uF="random_uniquessV.txt"
	sF="greedy_relSensV_fix.txt"



	random_choice=readFile(folder+cF)
	greedy_choice=readFile(folder+cgF)


	# random_choice=scale(random_choice)
	# greedy_choice=scale(greedy_choice)

	# choiceChange=greedy_choice-random_choice

	# random_choice*=2500000
	# greedy_choice*=2500000


	uniq=readFile(folder+uF)
	sen=readFile(folder+sF)

	# sen=[1-item for item in sen]
	#


	c=4000.0/2500000

	# fig = plt.figure()
	# axs = fig.add_subplot(111, projection='3d')

	fig, axs = plt.subplots(1,1,figsize=(4,3))

	# plt.set_cmap('afmhot')
	plt.set_cmap('Blues')
	axs.locator_params(axis='y',nbins=4)
	axs.locator_params(axis='x',nbins=4)
	# pos=random_choice.index(max(random_choice))
	# print random_choice[pos]
	# print uniq[pos]
 	#filterVector(uniq,sen,random_choice,folder+"randomM.txt",c)
 	#filterVector(uniq,sen,greedy_choice,folder+"greedyM.txt",c)

 	# uniqF,senF,choiceF=justFilter(uniq,sen,random_choice,c)
 	#done 
 	uniqF,senF,choiceF=justFilter(uniq,sen,greedy_choice,c)

 	cax=plt.scatter(uniqF,senF,s=30,c=choiceF,marker='o',alpha=0.6)

 	# maxChoice=roundup(max(choiceF))
 	maxChoice=max(choiceF)
 	mean=maxChoice/2
 	# mean=roundup(sum(choiceF)/len(choiceF))

 	# plt.ylabel(r'$VRR$',fontsize=16)
 	plt.ylabel('Reliablity Relevance',fontsize=14)
 	plt.xlabel('Uniqueness',fontsize=14)
 	plt.axis([0.1,1.2,0,1.2])
 	plt.title('DBLP',fontsize=12)
	# orientation='horizontal'
	# cbar=plt.colorbar(cax,ticks=[0,mean,maxChoice])
	# cbar.ax.set_yticklabels(['Zero', 'Medium', 'High'],fontsize=10) 
	#cbar.set_label('Sampling probability',fontsize=12)




	plt.show()

choicePlot()

