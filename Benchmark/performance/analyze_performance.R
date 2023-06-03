library(data.table)
library(ggplot2)


df <- fread("../../Testing/lab3_try.results.csv")
#df <- fread("../../Testing/lab3_try.significant.csv")

plink <- fread("~/lab3/lab3_gwas_covar.assoc.linear")

#top 10 hits 
plink_ordered <- plink[order(plink$P), c(2,9)]
print(head(plink_ordered))
print(head(df[, c(1,4)]))

#match rsid of both dataframes 
m1 <- match(df$snp, plink$SNP)
plink <- na.omit(plink[m1, ])
m2 <- match(plink$SNP, df$snp)
df <- na.omit(df[m2,])

print(all(df$snp == plink$SNP))#check to make sure snp order is matched 

us_p <- -log10(df$pvalues)
plink_p <- -log10(plink$P)

cor.test(us_p, plink_p) #r = 1
cor.test(us_p, plink_p)$p.value #p < 0

df_plot <- data.frame(us_p, plink_p)

plot <- ggplot(df_plot, aes(x = us_p, y = plink_p)) + 
	geom_point(color='darkblue') + 
	geom_abline(intercept = 0, slope = 1) + 
	labs(x="OUR TOOL: -log10(p) per snp", y = "PLINK: -log10(p) per snp") +
	theme_classic(base_size = 15)
ggsave(filename = "p_scatter.png", width = 8, height = 8)
