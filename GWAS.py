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
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

#---parse arguments
arg = argparse.ArgumentParser()
arg.add_argument('geno') #plink format
arg.add_argument("-p", dest = "plot", help = "If Plot shows", type = bool)
arg.add_argument("-sig", dest = "signficant", help = "only show genome-wide signficant variants", type = bool)
arg.add_argument("-sim", dest = "simulate", help = "run a simulation of GWAS without using real data, input a any ghost string for first argument and use this flag", type = bool)
arg.add_argument("-pca", dest = "pca", help = "control for principle components? default 3", type = bool)

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
    print("only output genome-wide significant hits")
if arguments.pca is True:
    print("automatically calculating top 3 PCs and adding them as covariates to the regression")

#---read in genotypes

if os.path.isfile((arguments.geno + ".bed")):
    bim,fam,geno  = pandas_plink.read_plink(arguments.geno)
    geno_matrix = geno.compute()
    df = pd.DataFrame({'snp' : bim.iloc[:,1]})
    pheno = fam['trait'].to_numpy() #REQUIRES PHENO TO BE IN 6TH COLUMN OF FAM FILE
else:
    print("invalid genotype file. make sure file exists")
    quit()


#format geno and pheno for linear regression 
geno = np.transpose(geno_matrix)
def floatit(i):
    return float(i)
pheno = list(map(floatit, pheno))

print("genotypes and phenotypes properly extracted and formatted")

#scale the genotypes
geno = scale.fit_transform(geno)
print("genotypes scaled")

#store betas and p values
betas = []
p_values = []


#pca 
if arguments.pca is True:
    print("computing principle components and including them into the regression")
    pca = 3
    os.system('plink --bfile ' + str(arguments.geno) + ' --out gwas_pca --pca ' + str(pca)) #create .eigenvec file
    pc = pd.read_csv("gwas_pca.eigenvec", header=None, delimiter=r"\s+")
    #extract pc columns as arrays
    pc1 = pc[2].to_numpy() 
    pc2 = pc[3].to_numpy() 
    pc3 = pc[4].to_numpy() 
    
    #linear regression including pcs
    for i in range(geno.shape[1]):
        #create matrix of snp, pc1, pc2, pc3
        X = np.concatenate((geno[:,i].reshape(-1, 1), pc1.reshape(-1, 1), pc2.reshape(-1, 1), pc3.reshape(-1, 1)), axis=1) 
        X = sm.add_constant(X)
        lm = sm.OLS(pheno, X, missing = 'drop').fit()
        betas.append(lm.params[1])
        p_values.append(lm.pvalues[1])

else:
    #linear regression for each snp no pc
    print("performing linear regression without principle componenets")
    for i in range(geno.shape[1]):
        X = geno[:,i].reshape(-1, 1)
        X = sm.add_constant(X)
        lm = sm.OLS(pheno, X, missing = 'drop').fit()
        betas.append(lm.params[1])
        p_values.append(lm.pvalues[1])


if arguments.plot is True:
    print("creating plots")
    #plot histogram of p values in 100 bins
    plt.hist(p_values, bins=1000)
    plt.savefig('lab3_pvalues.png')
    #plot manhattan

#make a dataframe of snps and p values
df['pvalues'] = p_values
df['beta'] = betas

#if user only wants significant hits, subset to those
#write a table of hits and their p values
if arguments.signficant is True:
    print("writing significant results to a csv file")
    significant_df = df[df['pvalues'] < 5e-8]
    significant_df.sort_values(by = 'pvalues', inplace = True)
    significant_df.to_csv("significant.csv", index = False)
else:
    print("writing all results to a csv file")
    df.sort_values(by = 'pvalues', inplace = True)
    df.to_csv("results.csv", index = False)




