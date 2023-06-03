library(data.table)
library(ggplot2)

df <- fread("big0.txt")
print(df)

ggplot(df, aes(x = X, y = runtime, group = tool, color = tool)) + 
	geom_line()+
  	theme_classic(base_size = 15)

ggsave(filename = "runtime.png")
