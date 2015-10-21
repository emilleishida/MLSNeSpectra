import numpy as np
ORG_DATA			= np.loadtxt('../data/derivatives.dat')
#############################
'''
#### REDUCTION_METHOD	 ####
possibilities:

-MeanShift
-KMeans

'''
#############################
REDUCTION_METHOD	= 'pca'
REDUCTION_PARS		= []
