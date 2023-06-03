library(data.table)

df <- fread("pigs.fam")

n <- nrow(df)

vec <- rep(c(0), each = n)

result <- data.frame(df$V1, df$V2, df$V3, df$V4, vec, df$V5)

write.table(result, file = "pigs.fam.edit", quote = F, row.names = F, col.names = F, sep = '\t')
