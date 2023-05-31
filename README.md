# CSE185FinalProject_GWAS

# Genome-wide association study to identify variant-trait associations
Our aim is to create a genome-wide association study (GWAS) tool to find significant variant-trait associations. Briefly, our tool takes in genotype data (variants) across people in plink bed/bim/fam format with the phenotype data per individual in the 6th column of the fam file. It outputs a csv file with effect size (𝜷) and a p-value for each snp (with options to limit to nominally significant snps). In addition, we aim to create a script to visualize GWAS data with a Manhattan plot. Our tool can be benchmarked against the plink --linear association test. Our tool is implemented as a python script. 

# Install Instructions 
`Python` must be installed to run the program. 

Install python through [this link](https://www.python.org/downloads/). Download the proper version for your device.
- Go to your command line and check to see if `Python` is installed with `python3 --version`.  
*Note: every command run through `python3` must be in the format `python3 [command]`.
- The Jupyter Notebook is a great alternative (instead of the command line).  

To implement many of the packages in python in your local directory, download Anaconda through [this link](https://www.anaconda.com/download).
- Once installed, type `ls` in your home directory and check if there is a directory `anaconda3`.
- Once `anaconda3` is in your home directory, you can proceed.
- Use the `pip install` format below in order to install the required packages.  
- Please make sure your device is plugged in before running `xcode-select --install`. This will take quite a while. This ensures that the the command like arguments such as `git clone [file]` can run correctly. 

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

If any of these python packages have to be installed, use the pip command to install it:  
*Note: if `anaconda3` is installed correctly, the terminal should say "Requirement already satisfied".
- `pip install numpy`
- `pip install statsmodels`
- `pip install -U matplotlib`
- `pip install pandas`
- `pip install argparse`
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
<!-- ![histogram_example](https://github.com/Lily-McCalmont/CSE185FinalProject_GWAS/blob/main/image.jpg?raw=true) -->

# Options
- `-p`: True = plot the distribution of p-values as a histogram. False = don't plot p-values
- `-sig`: True = save only nominally significant hits. False = save p-values and betas for all snps
- `-sim`: True = run simulation, without real genotype and phenotype data. please put a random file name as the path to plink files

# Outputs
- "significant.csv" = csv file of nominally significant hits. column 1 = snps, column 2 = p values, column 3 = betas
- "results.csv" = csv file of all associations. column 1 = snps, column 2 = p values, column 3 = betas
- "simulation_betas.png" = a histogram of betas when you use the simulated option
- "lab3_pvalues.png" = a histogram of p-values when you use the `-p True` option
  
# Examples 
*Note: Please remember, if running these commands from personal terminal the syntax is `python3` for all commands.  
To run a simulation: 

`python GWAS.py randomfile -sig True`
  
To run the testing data set from lab3:

`python GWAS.py Testing/lab3_try -p True -sig True`
  
# Recommendations
- if you are finding associations for a large number of snps, use nohup to run the program in the background

`nohup <command> &`
  
# Contributors
This repository was made by Kai Akamatsu, Rueshil Fadia, and Lily McCalmont with inspiration from plink --linear association test.
Please submit a pull request with any corrections or suggestions.
