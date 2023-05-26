import random
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import argparse
import pandas as pd
import os.path
import gzip
import pandas_plink


#---parse arguments
arg = argparse.ArgumentParser()
arg.add_argument('geno') #plink format
arg.add_argument("-p", dest = "plot", help = "If Plot shows", type = bool)
arg.add_argument("-sig", dest = "signficant", help = "only show signficant variants", type = bool)
arg.add_argument("-sim", dest = "simulate", help = "run a simulation of GWAS without using real data, input a any ghost string for first argument and use this flag", type = bool)

arguments = arg.parse_args()

if arguments.simulate is True:
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
    plt.hist(betas)
    plt.savefig('simulation_betas.png')
    quit()

if not os.path.isfile(arguments.geno + ".fam"):
    print("invalid phenotype file. make sure file exists")
    quit()

if arguments.plot is True:
    print("program will plot final manhattan plot and p value distribution")

if arguments.signficant is True:
    print("only output significant hits")


#---read in genotypes

if os.path.isfile((arguments.geno + ".bed")):
    bim,fam,geno  = pandas_plink.read_plink(arguments.geno)
    geno_matrix = geno.compute()
    print(geno_matrix.shape)
    df = pd.DataFrame({'snp' : bim.iloc[:,1]})
    print(df)
    pheno = fam['trait'].to_numpy() #REQUIRES PHENO TO BE IN 6TH COLUMN OF FAM FILE
    #print(pheno)
else:
    print("invalid genotype file. make sure file exists")
    quit()

#format geno and pheno for linear regression 
geno = np.transpose(geno_matrix)
#print(pheno.shape)
#print(geno.shape)
def floatit(i):
    return float(i)
pheno = list(map(floatit, pheno))


#linear regression for each snp
betas = []
p_values = []

for i in range(geno.shape[1]):
    lm = sm.OLS(pheno, geno[:,i].reshape(-1, 1), missing = 'drop').fit()
    #print(lm.pvalues[0])
    betas.append(lm.params[0])
    p_values.append(lm.pvalues[0])


if arguments.plot is True:
    #plot histogram of p values in 100 bins
    plt.hist(p_values, bins=1000)
    plt.savefig('lab3_pvalues.png')


#function to filter for nominally significant
def filter_nominal(i):
    return i < 0.05

#function to filter for genome-wide significant 
def filter_bonferroni(i):
    return i < 5e-8 #change to number of snps

#make a dataframe of snps and p values
df['pvalues'] = p_values
df['beta'] = betas

#if user only wants significant hits, subset to those
#write a table of hits and their p values
if arguments.signficant is True:
    significant_df = df[df['pvalues'] < 0.05]
    significant_df.sort_values(by = 'pvalues', inplace = True)
    significant_df.to_csv("significant.csv", index = False)
else:
    df.sort_values(by = 'pvalues', inplace = True)
    df.to_csv("results.csv")

#plot results? - manhattan




