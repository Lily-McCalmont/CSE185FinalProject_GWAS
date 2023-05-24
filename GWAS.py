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
