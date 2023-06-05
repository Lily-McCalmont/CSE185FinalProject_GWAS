import random
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import argparse
import pandas as pd
import os.path
import os
import gzip
import pandas_plink
from pandas import DataFrame
from scipy.stats import uniform
from scipy.stats import randint
import seaborn as sns

#Adapted from script below
#https://stackoverflow.com/questions/37463184/how-to-create-a-manhattan-plot-with-matplotlib-in-python
df = pd.read_csv("lab3_try.results.csv")
    
df = df.sort_values(['chrom', 'pos'])
df.reset_index(level = None, inplace = True, col_level = 0); 
df['xVal'] = df.index
df['yVal'] = -np.log10(df.pvalues); 
manhattan = sns.relplot(data=df, x='xVal', y='yVal', palette = 'colorblind', hue = 'chrom') 
groupedChrom=df.groupby('chrom')['xVal'].mean()
manhattan.ax.set_xticks(groupedChrom);
manhattan.ax.set_xticklabels(groupedChrom.index)
manhattan.ax.set_xlabel('chromosome'); 
manhattan.ax.set_ylabel('-log(p-val)'); 
manhattan.ax.set_ylim(0, 8)
manhattan.fig.suptitle('Plot of P-values per Chromosome');
plt.show()
