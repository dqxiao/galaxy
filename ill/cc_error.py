import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import numpy as np
# patterns = ('xx', '\\\\\\\\', '//')
methods=['Chamelon','Galaxy']
ks=[100,150,200,250,300]
markers=['^','o']
cs=['b','r']
labelFont=14
lwidth=3
legendFont=10

def create_df_dblp():
        raw_data = {'method_name': ['100', '150', '200', '250','300'],
        'Chamelon':  [0.005, 0.007, 0.008, 0.018, 0.042],
        'Galaxy':   [0.005, 0.006,  0.007, 0.01,0.012]
        }
        df = pd.DataFrame(raw_data, columns = ['method_name']+methods)

        return df 

def create_df_bright():
        raw_data = {'method_name': ['100', '150', '200', '250','300'],
        'Chamelon':  [0.067, 0.096, 0.149, 0.199, 0.242],
        'Galaxy':   [0.018,  0.02,  0.039, 0.099, 0.166]
        }
        df = pd.DataFrame(raw_data, columns = ['method_name']+methods)

        return df 



def create_df_ppi():
        raw_data = {'method_name': ['100', '150', '200', '250','300'],
        'Chamelon':  [0.051, 0.145, 0.245, 0.425, 0.625],
        'Galaxy':   [0.005,  0.089, 0.081, 0.207, 0.595]
        }
        df = pd.DataFrame(raw_data, columns = ['method_name']+methods)

        return df 


def make_line_plot(df,fig,ax,data):

        ax.plot(ks,df[methods[0]],color=cs[0],linewidth=lwidth,marker=markers[0],
                markerfacecolor='white', markeredgecolor=cs[0],markersize=10,mew=lwidth,
                label=methods[0])
        ax.hold(True)
        ax.plot(ks,df[methods[1]],color=cs[1],linewidth=lwidth,marker=markers[1],
                markerfacecolor='white', markeredgecolor=cs[1],markersize=10,mew=lwidth,
                label=methods[1])

       
        ax.locator_params(axis='y',nbins=5)

        ax.set_xlim([80,320])
        if data=="bright":
            ax.set_ylim([0,0.3])
        if data=="dblp":
            ax.set_ylim([0,0.05])
        if data=="ppi":
            ax.set_ylim([0,0.8])

        locSet="upper left"
        # if data=="ppi" or data=:
        #     locSet="upper left"
        # else:
        #     locSet="best"
        dataname=data
        if data=="bright":
            dataname="Brightkite"
        dataname=dataname.upper()
        ax.legend(methods, loc=locSet,ncol=1,numpoints=1,fontsize=legendFont)
        #setting label
        ax.set_xlabel("k",fontsize=labelFont)
        ax.set_ylabel('Relative Error \n Clustering Coefficient',fontsize=labelFont)
        # ax.set_title(dataname,fontsize=labelFont)

if __name__=="__main__":
        
         # done 

        
        
        data=sys.argv[1]
        
        if data=="ppi":
                df=create_df_ppi()
        if data=="bright":
                df=create_df_bright()
        if data=="dblp":
                df=create_df_dblp()

        fig, axs = plt.subplots(figsize=(4,3))


        # print df.min()

        make_line_plot(df,fig,axs,data)

        # plt.show()
        fig.savefig("./illOutput/"+data+"_cc.pdf")

        