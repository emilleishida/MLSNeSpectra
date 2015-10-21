from __future__ import print_function
from config import *
print('Main')

#############################
#### REDUCTION PART	 ####
#############################
exec('from reduction.'+REDUCTION_METHOD+' import reduction')
exec('from management.params_red import '+REDUCTION_METHOD+'_dict as dict_red')
def reduc(): np.savetxt('temp.dat',reduction(ORG_DATA,dict_red))

#############################
#### CLUSTERING PART	 ####
#############################
exec('from clustering.'+CLUSTERING_METHOD+' import clustering')
exec('from management.params_clust import '+CLUSTERING_METHOD+'_dict as dict_clust')
def cl_func(data): return clustering(data,dict_clust)
from clustering.plot import plot_clustering
def plot():	plot_clustering(cl_func,CL_DATA,CLUSTERING_METHOD)
