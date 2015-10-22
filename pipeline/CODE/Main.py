from __future__ import print_function
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(''))

from config import *
from management.update_dict import update_dict
from management.name_files import red_data_name,clust_name,plot_name

print('Main')

#############################
#### REDUCTION PART	 ####
#############################
exec('from management.params_red import '+REDUCTION_METHOD+'_dict as dict_red')
update_dict(dict_red,'RED_')
RED_DATA_NAME=red_data_name(REDUCTION_METHOD,dict_red)

def reduc():
	exec('from reduction.'+REDUCTION_METHOD+' import reduction')
	os.system('mkdir -p red_data')
	np.savetxt(RED_DATA_NAME,reduction(np.loadtxt(ORG_DATA),dict_red))

#############################
#### CLUSTERING PART	 ####
#############################
exec('from management.params_clust import '+CLUSTERING_METHOD+'_dict as dict_clust')
update_dict(dict_clust,'CL_')
CLUSTERS_DATA_NAME = clust_name(CLUSTERING_METHOD,dict_clust)
CLUSTERS_LABEL_NAME= clust_name(CLUSTERING_METHOD+'_label',dict_clust)

try:
	REDUCED_DATA_EXTERNAL
except NameError: RED_DATA=np.loadtxt(RED_DATA_NAME)
else		: RED_DATA=np.loadtxt(REDUCED_DATA_EXTERNAL)

def cluster():
	exec('from clustering.'+CLUSTERING_METHOD+' import clustering')
	os.system('mkdir -p cl_data')
	clusters,labels= clustering(RED_DATA,dict_clust)
	np.savetxt(CLUSTERS_DATA_NAME,clusters)
	np.savetxt(CLUSTERS_LABEL_NAME,labels)
	
try:
	CLUSTERS_DATA_EXTERNAL
except NameError: CL_DATA=np.loadtxt(CLUSTERS_DATA_NAME)
else		: CL_DATA=np.loadtxt(CLUSTERS_DATA_EXTERNAL)
try:
	LABELS_DATA_EXTERNAL
except NameError: LAB_DATA=np.loadtxt(CLUSTERS_LABEL_NAME)
else		: LAB_DATA=np.loadtxt(LABELS_DATA_EXTERNAL)

def plot():
	from ploting.plot import plot_data
	PLOT_NAME=plot_name(REDUCTION_METHOD,CLUSTERING_METHOD,dict_red,dict_clust,PLOT_EXT)
	os.system('mkdir -p plots')
	plot_data(RED_DATA.T,CL_DATA.T,LAB_DATA,PLOT_NAME)
