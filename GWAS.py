import random
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import sys
import getopt
import argparse
import pandas as pd
from os.path import join
from pandas_plink import read_plink
from pandas_plink import get_data_folder

arg = argparse.ArgumentParser()
arg.add_argument('file', type = argparse.FileType('r'))
arg.add_argument("-p", dest = "plot", help = "If Plot shows", type = bool)
arg.add_argument("-s", dest = "signficant", help = "only show signficant variants", type = bool)
arg.add_argument("-f", dest = "prefix", help = "prefix of files", type = str)

arguments = arg.parse_args()
array2 = []
array1 = []
for line in arguments.file: 
    array1.append(line)
    array2.append(array1)
    
    
x = function(array2, arguments.prefix, arguments.plot, arguments.signficant)

#----simualtion

random.seed(10)

#define simulation datasets (individuals, snps, maf)
num_individuals = 100
num_snps = 1000
maf = 0.2

#simulate genotypes as a matrix of people on rows, snps on columns (binomial distribution)
genotype_values = np.random.binomial(2, 0.2, size=(1000, 10000))
#print(genotype_values.shape) #check 1000 individuals, 10000 snps

#simulate phenotypes as a normal distribution 
phenotype_values = np.random.normal(size=1000)

#GWAS - for each snp compute the Beta from linear regression - store in a list? 
betas = []
p_values = []

# Create a linear regression model to find coefficients of every snp:
for i in range(num_snps):
    lm = sm.OLS(phenotype_values, genotype_values[:,i].reshape(-1, 1)).fit()
    betas.append(lm.params[0])
    p_values.append(lm.pvalues[0])

#plot the distribution of effect sizes of each snp 
#plt.hist(betas)
#plt.show()

#function to filter for nominally significant
def filter_nominal(i):
    return i < 0.05

#function to filter for genome-wide significant 
def filter_bonferroni(i):
    return i < 5e-8 #change to number of snps

print(list(filter(filter_nominal, p_values)))

#bonferroni correct the p values 

#report significant hits 

#write a table of all hits and their p values are z scores

#plot results? - manhattan



#--- lab plink datasets 





#--- real life dataset
