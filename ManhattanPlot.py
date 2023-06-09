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

parser = argparse.ArgumentParser()
parser.add_argument("file", help="path to csv file of results", type=str)
args = parser.parse_args()

df = pd.read_csv(args.file)
df = df.sort_values(['chrom', 'pos'])
df.reset_index(level = None, inplace = True, col_level = 0); 
df['x'] = df.index
df['-log10(p)'] = -np.log10(df['pvalues'])
group = df.groupby('chrom')['x'].mean()
plt.figure(figsize = (13, 6))
plt.scatter(df['x'], df['-log10(p)'], c = df['chrom'], cmap = 'rainbow')
plt.xticks(group, group.index)
plt.xlabel('Chromosomal position')
plt.ylabel('-log10(p)')
plt.colorbar(label = 'chrom')
plt.axhline(y=-np.log10(5e-8), color='red', linestyle='--')
plt.tight_layout()
plt.savefig('manhattan.png')
plt.show()
