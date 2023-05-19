import random
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt

#----simualtion

random.seed(10)

#define simulation datasets (individuals, snps, maf)
num_individuals = 100
num_snps = 1000
maf = 0.2

#simulate genotypes as a matrix of people on rows, snps on columns (binomial distribution)
genotype_values = np.random.binomial(2, 0.2, size=(1000, 10000))
print(genotype_values.shape) #check 1000 individuals, 10000 snps

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

#extract p values using the distribution of effect sizes of each snp 
plt.hist(betas)
plt.show()

#bonferroni correct the p values 

#report significant hits 

#write a table of all hits and their p values are z scores

#plot results? 



#--- lab plink datasets 





#--- real life dataset