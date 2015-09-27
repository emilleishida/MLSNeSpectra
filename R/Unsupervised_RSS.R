# First try Unsupervised 
require(RDRToolbox)
require(mclust)
spect<-read.table("..//data/derivatives_orig.dat",header=F)

s<-as.matrix(spect)


proj = LLE(data=s, dim=6, k=10)

mod = Mclust(as.data.frame(proj))
summary(mod, parameters = TRUE)

labels=mod$classification

proj2 <- Isomap(proj, dims = 3, k = 5)
proj22 <- as.data.frame(proj2)

plotDR(data=proj22,labels=labels)

