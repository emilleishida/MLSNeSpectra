from __future__ import print_function
from config import *
print('Main')

#############################
#### REDUCTION PART	 ####
#############################
exec('from reduction.'+REDUCTION_METHOD+' import reduction')
def reduc(): np.savetxt('temp.dat',reduction(ORG_DATA,REDUCTION_PARS))

#############################
#### CLUSTERING PART	 ####
#############################
exec('from clustering.'+CLUSTERING_METHOD+' import clustering')
def cl_func(data): return clustering(data,CLUSTERING_PARS)
from clustering.plot import plot_clustering
def plot():	plot_clustering(cl_func,CL_DATA,CLUSTERING_METHOD)
