
library(MVN)
genome_se <- read.delim("nucleotide_counts.txt",header = TRUE)
genome_inf<- genome_se[,3:9]
genome_inf_cor.pc <- princomp(genome_inf,cor=TRUE)
summary(genome_inf_cor.pc)
genome_inf_cor.pc$scores

par(pty="s")
plot(genome_inf_cor.pc$scores[,1], genome_inf_cor.pc$scores[,2],xlab="PC 1", ylab="PC 2", type ='n', lwd=2)
text(genome_inf_cor.pc$scores[,1], genome_inf_cor.pc$scores[,2], cex=0.9, lwd=2)
