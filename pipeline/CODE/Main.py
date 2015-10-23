from __future__ import print_function
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(''))

from config import *
from management.update_dict import update_dict
from management.name_files import red_data_name,clust_name,plot_name

def ERROR(message):
	out='### **ERROR** - '+message+' ####'
	line='\n'
	for x in out: line+='#'
	line+='\n'
	print(line+out+line)
	exit()
def READ(NAME):
	if os.path.isfile(NAME): return np.loadtxt(NAME)
	else: ERROR('file '+NAME+' does not exist!')


#############################
#### UPDATE DICTS AND	 ####
#### CREATE FILE NAMES	 ####
#############################
exec('from management.params_red import '+REDUCTION_METHOD+'_dict as dict_red')
update_dict(dict_red,'RED_')
RED_DATA_NAME=red_data_name(REDUCTION_METHOD,dict_red)

exec('from management.params_clust import '+CLUSTERING_METHOD+'_dict as dict_clust')
update_dict(dict_clust,'CL_')
CLUSTERS_DATA_NAME = clust_name(CLUSTERING_METHOD,dict_clust)
CLUSTERS_LABEL_NAME= clust_name(CLUSTERING_METHOD+'_label',dict_clust)

#############################
#### CHECK FOR EXT FILES ####
#############################
try:
	REDUCED_DATA_EXTERNAL
except NameError: RED_DATA,RED_TYPE=RED_DATA_NAME,REDUCTION_METHOD
else		: RED_DATA,RED_TYPE=REDUCED_DATA_EXTERNAL,'EXT';print('\t- using external reduced data')

try:
	CLUSTERS_DATA_EXTERNAL
except NameError: CL_DATA,CL_TYPE=CLUSTERS_DATA_NAME,CLUSTERING_METHOD
else		: CL_DATA,CL_TYPE=CLUSTERS_DATA_EXTERNAL,'EXT';print('\t- using external clusters')

try:
	LABELS_DATA_EXTERNAL
except NameError: LAB_DATA=CLUSTERS_LABEL_NAME
else		: LAB_DATA=LABELS_DATA_EXTERNAL;print('\t- using external labels')
	
#############################
#### REDUCTION PART	 ####
#############################
def reduc():
	exec('from reduction.'+REDUCTION_METHOD+' import reduction')
	os.system('mkdir -p red_data')
	try:
		ORG_DATA
	except NameError: ERROR('ORG_DATA key missing!')
	else:	np.savetxt(RED_DATA_NAME,reduction(READ(ORG_DATA),dict_red))

#############################
#### CLUSTERING PART	 ####
#############################
def cluster():
	exec('from clustering.'+CLUSTERING_METHOD+' import clustering')
	os.system('mkdir -p cl_data')
	clusters,labels= clustering(READ(RED_DATA),dict_clust)
	np.savetxt(CLUSTERS_DATA_NAME,clusters)
	np.savetxt(CLUSTERS_LABEL_NAME,labels)
	
#############################
#### QUALITY CHECK PART	 ####
#############################
def check_quality(METHOD):
	exec ('from quality.'+METHOD+' import quality')
	q=qual(READ(RED_DATA),LAB_DATA)
	return q
def do_quality():
	try:
		QUALITY_METHODS
	except NameError: ERROR('QUALITY_METHODS key missing!')
	else:
		used=False
		for METHOD in QUALITY_METHODS:
			if METHOD!='':	print('\t quality from',METHOD,':',check_quality(METHOD));used=True
		if used==False: print('\t<no quality checks>')

#############################
#### PLOTTIING PART	 ####
#############################
def plot():
	from ploting.plot import plot_data
	PLOT_NAME=plot_name(RED_TYPE,CL_TYPE,dict_red,dict_clust,PLOT_EXT)
	os.system('mkdir -p plots')
	plot_data(READ(RED_DATA).T,READ(CL_DATA).T,LAB_DATA,PLOT_NAME)
