# First try Unsupervised 
require(RDRToolbox)
require(mclust)
require(clValid)
require(kohonen)
require(NbClust)
spect<-read.table("..//data/derivatives.dat",header=F)

s<-as.matrix(spect)
proj = LLE(data=s, dim=5, k=10)

mod = Mclust(as.data.frame(proj))
summary(mod, parameters = TRUE)

labels=mod$classification
plotDR(data=proj,labels=labels)



# Cluster validation 


intern<-clValid()


data(mouse)


# Number of clusters via brute-force

Nc<-NbClust(proj,method="complete")

## internal validation



intern <- clValid(as.data.frame(proj), 2:6, clMethods=c("hierarchical","kmeans","som", "sota"),
                  validation="internal")
summary(intern)

plot(intern)
