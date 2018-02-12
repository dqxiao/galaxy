import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import numpy as np
# patterns = ('xx', '\\\\\\\\', '//')
methods=['RSME','NSC','RSME+','NSC+']
ks=[100,150,200]
markers=['^','o']
cs=['b','r']
labelFont=14
lwidth=3


def create_df_ppi_sample():
        raw_data = {'method_name': ['100', '150','200'],
        'RSME':  [0.094, 0.266, 0.331],
        'NSC':   [0.051, 0.115, 0.145],
        'RSME+':[0.093,0.27,0.341],
        'NSC+':[0.054,0.106,0.14]
        }
        df = pd.DataFrame(raw_data, columns = ['method_name']+methods)

        return df 



def make_line_plot(df,fig,ax,data):

        ax.plot(ks,df[methods[0]],color=cs[0],linewidth=lwidth,marker=markers[0],
                markerfacecolor='white', markeredgecolor=cs[0],markersize=8,mew=lwidth,
                label=methods[0])
        ax.hold(True)

        ax.plot(ks,df[methods[2]],'--',color=cs[0],linewidth=lwidth,marker=markers[0],
                markerfacecolor='white', markeredgecolor=cs[0],markersize=8,mew=lwidth,
                label=methods[2])
        ax.hold(True)

        ax.plot(ks,df[methods[1]],color=cs[1],linewidth=lwidth,marker=markers[1],
                markerfacecolor='white', markeredgecolor=cs[1],markersize=8,mew=lwidth,
                label=methods[1])
        ax.hold(True)

        ax.plot(ks,df[methods[3]],'--',color=cs[1],linewidth=lwidth,marker=markers[1],
                markerfacecolor='white', markeredgecolor=cs[1],markersize=8,mew=lwidth,
                label=methods[3])

       
        ax.locator_params(axis='y',nbins=5)

        ax.set_xlim([80,220])
        ax.set_ylim([0,0.5])
        locSet='upper left'
        dataname=data
        if data=="bright":
            dataname="Brightkite"
        ax.legend(methods, loc=locSet,ncol=2,numpoints=1,fontsize=8)
        #setting label
        ax.set_xlabel("k",fontsize=labelFont)
        ax.set_ylabel('Relative Error \n Average Distance',fontsize=labelFont)
        ax.set_title(dataname,fontsize=labelFont)

if __name__=="__main__":
        
         # done 

        
        
        data=sys.argv[1]
        
        df=create_df_ppi_sample()

        fig, axs = plt.subplots(figsize=(4,3))


        # print df.min()

        make_line_plot(df,fig,axs,data)

        # plt.show()
        fig.savefig("./illOutput/"+data+"_apd+.pdf")

        