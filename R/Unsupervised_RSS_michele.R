# First try Unsupervised 
require(RDRToolbox)
require(mclust)
require(lle)
#spect<-read.table("..//data/derivatives_orig.dat",header=F)
#spect<-read.table("..//data/derivatives.dat",header=F)
#spect<-read.table("..//data_all_epochs/derivatives_orig.dat",header=F)
spect<-read.table("..//data_all_epochs/derivatives.dat",header=F)
s<-as.matrix(spect)

# select a range of epochs
names<-read.table('../data_all_epochs/SNe.txt',header=F)
SNe=names[1]
epochs=names[2]
aux = which(epochs > -2.5)
aux = aux[which(epochs[aux,] < 2.5)]
#epochs[aux,]
s=s[aux,]



n_k=10

lle_dim=5

###############
#proj = LLE(data=s, dim=lle_dim, k=n_k)
#
#mod = Mclust(as.data.frame(proj))
#summary(mod, parameters = TRUE)
#
#labels=mod$classification
#
#proj2 <- Isomap(proj, dims = 3, k = n_k)
#proj22 <- as.data.frame(proj2)
#
#plotDR(data=proj22,labels=labels)
###############

##############
results = lle(X=s, m=lle_dim, k=n_k, id=TRUE, iLLE=TRUE, v=.90)

mod = Mclust(as.data.frame(results$Y))
summary(mod, parameters = TRUE)

labels=mod$classification

str( results )

# plot results and intrinsic dimension (manually)
split.screen( c(2,1) )
screen(1)
plot( results$Y, main="embedded data", xlab=expression(y[1]), ylab=expression(y[2]) )
screen(2)
plot( results$id, main="intrinsic dimension", type="l", xlab=expression(x[i]), ylab="id", lwd=2 )

proj2_lle <- Isomap(results$Y, dims = 3, k = n_k)
proj22_lle <- as.data.frame(proj2_lle)

plotDR(data=proj22_lle,labels=labels)
##############


