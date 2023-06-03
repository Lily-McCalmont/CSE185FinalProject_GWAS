time python ../../GWAS.py ../../Testing/lab3_try

time plink --vcf ~/public/lab3/lab3_gwas.vcf.gz --pheno ~/public/lab3/lab3_gwas.phen --linear --maf 0.05 --no-sex --out lab3_benchmark

