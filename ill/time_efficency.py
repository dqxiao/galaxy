import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import ScalarFormatter
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
        'Chameleon':  [4.3E+07,4.4E+07,4.68E+07,4.74E+07,5.05E+07],
        'Galaxy':     [3.36E+07,4.7E+07,4.89E+07, 5.20E+07,5.43E+07]
        }
        df = pd.DataFrame(raw_data, columns = ['method_name']+methods)

        return df 

def create_df_bright():
        raw_data = {'method_name': ['100', '150', '200', '250','300'],
        'Chameleon':  [215785,303656,391528,518478,645429],
        'Galaxy':   [246365,332723,419081,522744,626407]
        }
        df = pd.DataFrame(raw_data, columns = ['method_name']+methods)

        return df 



def create_df_ppi():
        raw_data = {'method_name': ['100', '150', '200', '250','300'],
        'Chameleon':  [174071, 332496, 490922, 742957, 994993],
        'Galaxy':   [166751, 388660,610570, 735576, 860583]
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

        y_formatter=ScalarFormatter(useMathText=True)
        y_formatter.set_powerlimits((5,5))

        ax.set_xlim([80,320])
        # 
        if data=="ppi":
            ax.set_ylim([0,1200000])
        if data=="bright":
            ax.set_ylim([0,800000])
        if data=="dblp":
            ax.set_ylim([2E+07,6.2E+07])

        locSet="lower right"
        dataname=data
        if data=="bright":
            dataname="Brightkite"
        ax.legend(methods, loc=locSet,ncol=1,numpoints=1,fontsize=legendFont)
        #setting label
        ax.yaxis.set_major_formatter(y_formatter)
        ax.set_xlabel("k",fontsize=labelFont)
        ax.set_ylabel('Runing Time(ms)',fontsize=labelFont)
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
        fig.savefig("./illOutput/"+data+"_time.pdf")