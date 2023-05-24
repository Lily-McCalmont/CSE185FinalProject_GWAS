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
arg.add_argument('phenotype')
arg.add_argument("-p", dest = "plot", help = "If Plot shows", type = bool)
arg.add_argument("-sig", dest = "signficant", help = "only show signficant variants", type = bool)
arg.add_argument("-g", dest = "geno", help = "path to genotype file in plink format", type = str) #plink prefix 

arguments = arg.parse_args()

if not os.path.isfile(arguments.phenotype):
    print("invalid phenotype file. make sure file exists")
    quit()

if arguments.plot is True:
    print("program will plot final result")

if arguments.signficant is True:
    print("only output significant hits")

#--- for reading in vcf file using pandas - need name of columns
def read_vcf_names(vcf):
    with gzip.open(vcf, "rt") as file:
          for l in file:
            if l.startswith("#CHROM"):
                  names = [x for x in l.split('\t')]
                  break
    file.close()
    return names

#---read in genotypes

if os.path.isfile(arguments.geno):
    bim,fam,geno  = pandas_plink.read_plink(arguments.geno)
    geno_matrix = geno.compute()
    print(geno_matrix)
else:
    print("invalid genotype file. make sure file exists")
    quit()


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
