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

CLUSTERING_METHOD	= 'KMeans'
CL_n_clusters=10


#CLUSTERING_METHOD	= 'AgglomerativeClustering'
