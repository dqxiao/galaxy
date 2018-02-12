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
        'Chamelon':  [0.06, 0.117, 0.19, 0.263, 0.411],
        'Galaxy':   [0.039, 0.066,  0.088, 0.12,0.143]
        }
        df = pd.DataFrame(raw_data, columns = ['method_name']+methods)

        return df 


def create_df_ppi():
        raw_data = {'method_name': ['100', '150', '200', '250','300'],
        'Chamelon':  [0.024, 0.33, 1.458, 1.636, 3.106],
        'Galaxy':   [0.048,  0.29,  0.553, 0.828,1.081]
        }
        df = pd.DataFrame(raw_data, columns = ['method_name']+methods)

        return df 

def create_df_bright():
        raw_data = {'method_name': ['100', '150', '200', '250','300'],
        'Chamelon':  [0.145, 0.394, 0.628, 0.936, 1.48],
        'Galaxy':   [0.095,  0.251, 0.393, 0.562,0.758]
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
       
        if data=="ppi":
            ax.set_ylim([0,4])
        if data=="bright":
            ax.set_ylim([0,2])
        if data=="dblp":
            ax.set_ylim([0,0.5])  
        # else:
        #     locSet="best"
        locSet="upper left"
        dataname=data
        if data=="bright":
            dataname="Brightkite"
        dataname=dataname.upper()

        ax.legend(methods, loc=locSet,ncol=1,numpoints=1,fontsize=legendFont)
        
        ax.set_xlabel("k",fontsize=labelFont)
        ax.set_ylabel('Relative Error \n Degree',fontsize=labelFont)
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
        fig.savefig("./illOutput/"+data+"_degree.pdf")

        