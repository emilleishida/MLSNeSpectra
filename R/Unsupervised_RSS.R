# First try Unsupervised 
require(RDRToolbox)
require(mclust)
spect<-read.table("..//data/derivatives.dat",header=F)

s<-as.matrix(spect)
proj = LLE(data=s, dim=3, k=10)

mod = Mclust(as.data.frame(proj))
summary(mod, parameters = TRUE)

labels=mod$classification
plotDR(data=proj,labels=labels)