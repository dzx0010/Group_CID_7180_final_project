#Set the working directory
#Make sure the files from the Bash script or in the same directory
setwd('~/Phylogenetic_Tree')

#Make sure all packages are installed
#Install if needed and load packages.

#devtool package need in order to install phangorn
install.packages('devtools')

#Install packages that provide the basis for manipulating sequence data in R: ape and phangorn.
install.packages("ape")
install.packages("phangorn")

#Load packages
library(ape)
library(phangorn)

#Create the tree after aligning with clustal and estimating tree with phyml
MyTree <- read.tree("out_allseq.phy_phyml_tree")
colors <- rainbow(Nedge(MyTree)) #add colors to the branches
plot(MyTree, edge.color=colors)
pdf("Tree.pdf") #saving the plot as a pdf
dev.off()
