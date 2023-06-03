#set up plink files that are subset 

for n in 100 500 2000 5000 10000
do 
	plink --bfile ../../Testing/lab3_try --extract plink_subsets/$n.txt --out plink_subsets/$n --make-bed
done



echo "computing runtime big O"

for n in 100 500 2000 5000 10000
do 
	time python ../../GWAS.py plink_subsets/$n

	time plink --bfile plink_subsets/$n --pheno ../../Testing/lab3_gwas.phen --linear --maf 0.05 --no-sex --out output/$n

done
