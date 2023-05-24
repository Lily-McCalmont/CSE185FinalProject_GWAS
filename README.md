# CSE185FinalProject_GWAS

# Genome-wide association study to identify variant-trait associations
Our aim is to create a genome-wide association (GWA) test to find significant variant-trait associations. Briefly, our tool will take in genotype data (variants) across people in plink bed/bim/fam format along with their phenotype data and output an effect size (𝜷) and a p-value for each snp. In addition, we aim to create a script to visualize GWAS data with a Manhattan plot. Our tool can be benchmarked against the plink --linear association test. We will implement our tool as a python script with genotype and phenotype files to test our script. 

# Install Instructions
Installation requires `random`, `numpy as np`, `statsmodels.api`, and `matplotlib.pylot`. 

```  
import statsmodels.api as sm  
import matplotlib.pyplot as plt
```

# Basic Uses
Basic usage:

command line -> 

To run in test examples:
command line ->  

When running the histogram plotting code with the given test values the plot should look like this:   

# Options
The required input:  

- `-f``--fasta FILE`: 
- `-r``--region REG`:
- `-o``--output FILE`:

# Contributors
This repository was made by Kai Akamatsu, Rueshil Fadia, and Lily McCalmont with inspiration from plink --linear association test.

Please submit a pull request with any corrections or suggestions.
