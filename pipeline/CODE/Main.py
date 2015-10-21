from __future__ import print_function
from config import *
from management.update_dict import update_dict
import numpy as np
import os
print('Main')

#############################
#### REDUCTION PART	 ####
#############################
exec('from management.params_red import '+REDUCTION_METHOD+'_dict as dict_red')
update_dict(dict_red,'RED_')

from management.name_files import red_data_name,clust_name
RED_DATA_NAME=red_data_name(REDUCTION_METHOD,dict_red)


exec('from reduction.'+REDUCTION_METHOD+' import reduction')
def reduc():
	os.system('mkdir -p red_data')
	np.savetxt(RED_DATA_NAME,reduction(np.loadtxt(ORG_DATA).T,dict_red))

#############################
#### CLUSTERING PART	 ####
#############################
exec('from management.params_clust import '+CLUSTERING_METHOD+'_dict as dict_clust')
update_dict(dict_clust,'CL_')

exec('from clustering.'+CLUSTERING_METHOD+' import clustering')
def cl_func(data): return clustering(data,dict_clust)


CLUSTERING_OUT_NAME=clust_name(CLUSTERING_METHOD,dict_clust)
from clustering.plot import plot_clustering
def plot():
	try:
		CLUSTERING_DATA
	except NameError: CL_DATA=np.loadtxt(RED_DATA_NAME).T
	else		: CL_DATA=np.loadtxt(CLUSTERING_DATA).T
	plot_clustering(cl_func,CL_DATA,CLUSTERING_OUT_NAME)
