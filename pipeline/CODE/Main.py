from __future__ import print_function
from config import *
from management.update_dict import update_dict
print('Main')

#############################
#### REDUCTION PART	 ####
#############################
exec('from management.params_red import '+REDUCTION_METHOD+'_dict as dict_red')
update_dict(dict_red,'RED_')

from management.red_data_name import red_data_name
RED_DATA_NAME=red_data_name(REDUCTION_METHOD,dict_red)

exec('from reduction.'+REDUCTION_METHOD+' import reduction')
def reduc(): np.savetxt(RED_DATA_NAME,reduction(ORG_DATA,dict_red))

#############################
#### CLUSTERING PART	 ####
#############################
exec('from management.params_clust import '+CLUSTERING_METHOD+'_dict as dict_clust')
update_dict(dict_clust,'CL_')

exec('from clustering.'+CLUSTERING_METHOD+' import clustering')
def cl_func(data): return clustering(data,dict_clust)

try:
	CLUSTERING_DATA
except NameError: CL_DATA=np.loadtxt(RED_DATA_NAME)
else		: CL_DATA=np.loadtxt(CLUSTERING_DATA)

from clustering.plot import plot_clustering
def plot():	plot_clustering(cl_func,CL_DATA,CLUSTERING_METHOD)
