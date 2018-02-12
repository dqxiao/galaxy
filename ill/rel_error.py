import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import numpy as np
# patterns = ('xx', '\\\\\\\\', '//')
methods=['Chameleon','Galaxy']
ks=[100,150,200,250,300]
markers=['^','o']
cs=['b','r']
labelFont=14
lwidth=3
legendFont=10


def create_df_dblp():
        raw_data = {'method_name': ['100', '150', '200', '250','300'],
        'Chameleon':  [0.0242355,0.030866,0.0376112,0.0481555,0.0745492],
        'Galaxy':   [0.0232459,0.0266931,0.0347333,0.0434572,0.0481738]
        }
        df = pd.DataFrame(raw_data, columns = ['method_name']+methods)

        return df 

def create_df_bright():
        raw_data = {'method_name': ['100', '150', '200', '250','300'],
        'Chameleon':  [0.0224918,0.0478918,0.0858148,0.114907,0.145636],
        'Galaxy':   [0.0193175,0.0410166,0.0542794,0.0664746,0.0783708]
        }
        df = pd.DataFrame(raw_data, columns = ['method_name']+methods)

        return df 



def create_df_ppi():
        raw_data = {'method_name': ['100', '150', '200', '250','300'],
        'Chameleon':  [0.00406348, 0.0232305, 0.0746659, 0.0858497, 0.0970367],
        'Galaxy':   [0.00431239, 0.0172516, 0.0243524, 0.0287901, 0.0326597]
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
        # ax.set_ylim([0,0.5])
        if data=="ppi":
            locSet="upper left"
        else:
            locSet="upper left"
        dataname=data
        if data=="bright":
            dataname="Brightkite"
        ax.legend(methods, loc=locSet,ncol=1,numpoints=1,fontsize=legendFont)
        #setting label
        ax.set_xlabel("k",fontsize=labelFont)
        ax.set_ylabel('Average \n Reliablity Discrepancy',fontsize=labelFont)
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
        fig.savefig("./illOutput/"+data+"_rel.pdf")

        