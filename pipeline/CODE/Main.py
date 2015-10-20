from __future__ import print_function
from config import *

#############################
#### REDUCTION PART	 ####
#############################

# from reduction import ???


#############################
#### CLUSTERING PART	 ####
#############################
print('Main')
from clustering.MeanShift import func
from clustering.plot import plot_clustering
def cl_func(data): return func(data,CLUSTERING_PARS)
def plot():	plot_clustering(cl_func,CL_DATA,CLUSTERING_METHOD)
