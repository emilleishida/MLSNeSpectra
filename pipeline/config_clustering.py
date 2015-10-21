import numpy as np
CL_DATA			= np.loadtxt('../../MLSNeSpectra/empca_trained_coeff/coefficients.dat').T
CL_DATA			= np.loadtxt('temp.dat').T
N_CLUSTERS		= 3
#############################
'''
#### CLUSTERING_METHOD	 ####
possibilities:

-MeanShift
	params=[p1,p2,p3]
	-p1: 
	-p2: 
-KMeans

'''
#############################
CLUSTERING_METHOD	= 'MeanShift'
CLUSTERING_PARS		= [.05]

CLUSTERING_METHOD	= 'KMeans'
CLUSTERING_PARS		= []

CLUSTERING_METHOD	= 'AgglomerativeClustering'
CLUSTERING_PARS		= []
