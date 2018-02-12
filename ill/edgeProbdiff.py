import matplotlib.pyplot as plt 

from matplotlib import rcParams
import sys
rcParams.update({'figure.autolayout': True})
label_size = 10
rcParams['xtick.labelsize'] = label_size
rcParams['ytick.labelsize'] = label_size
rcParams['axes.linewidth'] = 1

def edgeProbDiffPlot():

	option=sys.argv[1]

	rep=[8.18e-06, 0, 0.4795, 0.367, 0.344, 0.144]   # updated using ADR method 
	# rep_AN=[1.21e-05, 0, 0.3677, 0.257, 0.202, 0.096] #updated using ADR method 
	rep_AN=[5.8138e-06,0,0.46,0.462838397511,0.34,0.18]
	AUG_RR=[5.00e-06, 0, 0.0185, 0.025, 0.032, 0.048]
	AUG_C=[5.26e-06, 0, 0.0054,0.010,0.024,0.050]
	AUG_CRR=[4.814e-06, 0, 0.0048, 0.009, 0.022, 0.044]


	x=[0,0.2,0.4,0.6,0.8, 1]

	# plt.plot(x,rep)
	labels=['RSME','RS','ME','Rep-An','Rep']
	linetypes=['-D','-<','-s','--o','-']
	col = {	'azure':(0.2,0.4,0.6), 
		'grey':(0.69,0.69,0.69), 
		'hotpink':(0.68,0.14,0.37),
		'black':(0,0,0), 
		'babyblue':(0.87,0.94,0.94),
		'violet':(0.5411764705882353, 0.16862745098039217, 0.8862745098039215),
		'royalblue':(0.2549019607843137, 0.4117647058823529, 0.8823529411764706),
		'crimson':(0.8627450980392157, 0.0784313725490196, 0.23529411764705882),
		'seagreen':(0.1803921568627451, 0.5450980392156862, 0.3411764705882353)
		}



	fig=plt.figure(figsize=(4,3))
	plt.title('DBLP',fontsize=12) # title:12
	if option=="1":
		plt.plot(x,AUG_CRR,linetypes[0],label=labels[0],linewidth=3.0,markersize=8,color='r',markeredgewidth=2.0,fillstyle='none')
		plt.plot(x,rep_AN, linetypes[3],label=labels[3],linewidth=3.0,markersize=8,color='k',markeredgewidth=2.0,fillstyle='none')
		plt.plot(x,rep, linetypes[4],label=labels[4],linewidth=3.0,markersize=8,color='k',markeredgewidth=2.0,fillstyle='none')
		plt.legend(loc=6,frameon=True,numpoints=1,fontsize=14)

	if option=="2":

		plt.plot(x,AUG_CRR,linetypes[0],label=labels[0],linewidth=2.0,markersize=8,color=col['crimson'],markeredgewidth=2.0,fillstyle='none')
		plt.plot(x,AUG_RR,linetypes[1],label=labels[1],linewidth=2.0,markersize=8,color='b',markeredgewidth=2.0,fillstyle='none')
		plt.plot(x,AUG_C,linetypes[2],label=labels[2],linewidth=2.0,markersize=8,color='c',markeredgewidth=2.0,fillstyle='none')
		plt.legend(loc=0,frameon=True,numpoints=1,fontsize=14)

	

	plt.xlabel('Edge Probability',fontsize=14)
	plt.ylabel('Mean Absoulute Error', fontsize=14)
	plt.show()



edgeProbDiffPlot()




