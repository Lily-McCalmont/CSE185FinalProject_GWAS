# CSE185FinalProject_GWAS

# Genome-wide association study to identify variant-trait associations
Our aim is to create a genome-wide association study (GWAS) tool to find significant variant-trait associations. Briefly, our tool takes in genotype data (variants) across people in plink bed/bim/fam format with the phenotype data per individual in the 6th column of the fam file. It outputs a csv file with effect size (𝜷) and a p-value for each snp (with options to limit to genome-wide significant snps). In addition, we aim to create a script to visualize GWAS data with a Manhattan plot. Our tool can be benchmarked against the plink --linear association test.

# Install Instructions 
`Python` must be installed to run the program. 

Install python through [this link](https://www.python.org/downloads/). Download the proper version for your device.
- Go to your command line and check to see if `Python` is installed with `python3 --version` or `python --version`.  
*Note: every command run through `python3` must be in the format `python3 [command]`.
- The Jupyter Notebook is a great alternative (instead of the command line).  

To install many important packages that are commonly used in python, download Anaconda through [this link](https://www.anaconda.com/download).
- Once installed, type `ls` in your home directory and check if there is a directory `anaconda3`.
- Once `anaconda3` is in your home directory, you can proceed.
- Use the `pip install` format below in order to install the required packages.  
- Use `pip install GitPython` to install git.
- If there is an error cloning the repository, run `xcode-select --install`. Please make sure your device is plugged in before running. This will take quite a while. This ensures that the the command line arguments such as `git clone [file]` can run correctly if there is an error. 

`Plink` must be installed to run the program. 
Install plink through [this link](https://www.cog-genomics.org/plink/).

The program requires the following python packages:
- `random`
- `numpy`
- `statsmodels.api`
- `matplotlib.pylot`
- `argparse`
- `pandas`
- `os.path`
- `gzip`
- `pandas_plink`
- `scikit-learn`
- `seaborn`

If any of these python packages have to be installed, use the pip command to install it:  
*Note: `anaconda3` will automatically download all packages except pandas-plink which you will have to install manually. If `anaconda3` is installed correctly, the terminal should say "Requirement already satisfied".
- `pip install numpy`
- `pip install statsmodels`
- `pip install -U matplotlib`
- `pip install pandas`
- `pip install argparse`
- `pip install -U scikit-learn`
- `pip install seaborn`
- `conda install -c conda-forge pandas-plink`   

*Note: installing pandas-plink will take a little bit, but make sure to click `y` in order to proceed with the download.

# Clone the repository locally
In your terminal, run the following:
- `git clone <link to repository>`
- `cd CSE185FinalProject_GWAS`
- Type `ls` and check that all the appropriate files are displayed.

# Available files for testing
in the "Testing" directory, we have included examples of properly formatted inputs
- plink files with prefix: "lab3_try"

# Basic Uses
Basic usage:

`python GWAS.py <path to plink files> [options (see below) ] `

- "path to plink files" should be in the plink prefix form: "plinkfile" instead of "plinkfile.bim" (bed/fam)

When running the simulation (100 individuals, 1,000 snps, maf = 0.2) to see the distribution of betas, the plot should look like this:  

![image](https://github.com/Lily-McCalmont/CSE185FinalProject_GWAS/assets/134024621/5fc22cdc-263d-48c5-8fbc-7363074e7e16) 

# Options
- `-p`: make a Manhattan plot: chromosomal position on the X axis and -log10(p) on the Y axis
- `-sig`: save only genome-wide significant hits, otherwise output all snps
- `-sim`: run simulation, without real genotype and phenotype data. please put a random file name as the path to plink files
- `-pca`: compute and control for top 3 principle components, otherwise don't control of pcs

# Outputs
The outputs from our program will be files that must be opened and viewed. These include:
- "significant.csv" = csv file of gennome-wide significant hits.
- "results.csv" = csv file of all associations.
- "simulation_betas.png" = a histogram of betas when you use the simulated option
- "manhattan.png" = a manhattan plot which represents the p-values of chromosomes
- "lab3_pvalues.png" = a histogram of p-values when you use the `-p True` option
- "gwas_pca" eigenvec/eigenval/log/nosex = intermediate files of pca   
  
# Examples 
To run a simulation: 

`python GWAS.py randomfile -sim`
  
To run the testing dataset from lab3 while controlling pcs and output only genome-wide significant results:

`python GWAS.py Testing/lab3_try -p -sig -pca`
  
# Recommendations
- if you are finding associations for a large number of snps, use nohup to run the program in the background

`nohup <command> &`
  
# Contributors
This repository was made by Kai Akamatsu, Rueshil Fadia, and Lily McCalmont with inspiration from plink --linear association test.
Please submit a pull request with any corrections or suggestions.
