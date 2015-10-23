from __future__ import print_function
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(''))

from config import *
from management.update_dict import update_dict
from management.name_files import create_name,plot_name
from management.info_work import prt,print_info,read_info

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

print('''
################################################
########## BEGINNING PIPELINE HMV ##############
################################################
''')

#############################
#### UPDATE DICTS AND	 ####
#### CREATE FILE NAMES	 ####
#############################
exec('from management.params_red import '+REDUCTION_METHOD+'_dict as dict_red')
update_dict(dict_red,REDUCTION_METHOD)
RED_DATA_NAME=create_name(REDUCTION_METHOD,dict_red,'red_data/reduced_data_')

exec('from management.params_clust import '+CLUSTERING_METHOD+'_dict as dict_clust')
update_dict(dict_clust,CLUSTERING_METHOD)
CLUSTERS_DATA_NAME = create_name(CLUSTERING_METHOD,dict_clust,'cl_data/clustering_')
CLUSTERS_LABEL_NAME= create_name(CLUSTERING_METHOD+'_label',dict_clust,'cl_data/clustering_')

info_dir='info/'
os.system('mkdir -p '+info_dir)
info_sufix='.info'
REDUCTION_INFO	= info_dir + 'reduction' 	+ info_sufix
CLUSTER_INFO	= info_dir + 'clustering'	+ info_sufix
QUALITY_INFO	= info_dir + 'quality'		+ info_sufix
PLOT_INFO	= info_dir + 'plot'		+ info_sufix
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
	try:
		REDUCED_DATA_EXTERNAL
	except NameError: pass
	else		: print ("REDUCED_DATA_EXTERNAL is defined, please check what you realy want to do!"); exit()
	exec('from reduction.'+REDUCTION_METHOD+' import reduction')
	os.system('mkdir -p red_data')
	try:
		ORG_DATA
	except NameError: ERROR('ORG_DATA key missing!')
	else:	
		np.savetxt(RED_DATA_NAME,reduction(READ(ORG_DATA),dict_red))
		print_info(REDUCTION_METHOD,dict_red,'### REDUCTION USED ###',REDUCTION_INFO)

#############################
#### CLUSTERING PART	 ####
#############################
def cluster():
	try:
		CLUSTERS_DATA_EXTERNAL
	except NameError: pass
	else		: print ("CLUSTERS_DATA_EXTERNAL is defined, please check what you realy want to do!"); exit()
	exec('from clustering.'+CLUSTERING_METHOD+' import clustering')
	os.system('mkdir -p cl_data')
	clusters,labels= clustering(READ(RED_DATA),dict_clust)
	np.savetxt(CLUSTERS_DATA_NAME,clusters)
	np.savetxt(CLUSTERS_LABEL_NAME,labels)
	try:
		REDUCED_DATA_EXTERNAL
	except NameError: RED_PROP=open(REDUCTION_INFO,'r').read()
	else		: RED_PROP='### REDUCTION USED ###\nfrom external data = '+REDUCED_DATA_EXTERNAL
	prt(CLUSTER_INFO,RED_PROP,'w')
	print_info(CLUSTERING_METHOD,dict_clust,'### CLUSTERING USED ###',CLUSTER_INFO,'a')
	prt(CLUSTER_INFO,'\n\t-outputs:','a')
	prt(CLUSTER_INFO,'n_clusters = '+str(clusters.shape[0]),'a')
	
#############################
#### QUALITY CHECK PART	 ####
#############################
def check_quality(METHOD):
	exec('from management.params_quality import '+METHOD+'_dict as dict_qual')
	update_dict(dict_qual,METHOD)
	exec ('from quality.'+METHOD+' import quality')
	q=quality(READ(RED_DATA),READ(CL_DATA),READ(LAB_DATA),dict_qual)
	return q
def do_quality():
	try:
		QUALITY_METHODS
	except NameError: ERROR('QUALITY_METHODS key missing!')
	else:
		used=False
		try:
			CLUSTERS_DATA_EXTERNAL
		except NameError: CL_PROP=open(CLUSTER_INFO,'r').read()
		else		: CL_PROP='### CLUSTERS USED ###\nfrom external data = '+CLUSTERS_DATA_EXTERNAL
		prt(QUALITY_INFO,CL_PROP,'w')
		prt(QUALITY_INFO,'### QUALITIES USED ###','a')
		for METHOD in QUALITY_METHODS:
			print_info(METHOD,dict_clust,'',QUALITY_INFO,'a')
		prt(QUALITY_INFO,'\n\t-outputs:','a')
		for METHOD in QUALITY_METHODS:
			if METHOD!='':
				q=check_quality(METHOD)
				print('\tquality from',METHOD,':',q)
				prt(QUALITY_INFO,'quality from '+METHOD+' = '+str(q),'a')
				used=True
		if used==False:
			print('\t<no quality checks>')
			prt(QUALITY_INFO,'\t<no quality checks>')

#############################
#### PLOTTIING PART	 ####
#############################
def plot():
	from ploting.plot import plot_data
	PLOT_NAME=plot_name(RED_TYPE,CL_TYPE,dict_red,dict_clust,PLOT_EXT)
	os.system('mkdir -p plots')
	plot_data(READ(RED_DATA).T,READ(CL_DATA).T,READ(LAB_DATA),PLOT_NAME)
	try:
		CLUSTERS_DATA_EXTERNAL
	except NameError: CL_PROP=open(CLUSTER_INFO,'r').read()
	else		: CL_PROP='### CLUSTERS USED ###\nfrom external data = '+CLUSTERS_DATA_EXTERNAL
	prt(PLOT_INFO,CL_PROP,'w')
