#############################
'''
Original data:
	Used for the reduction,
	not needed if doing clusreing only
'''
#############################
ORG_DATA			= '../data/derivatives.dat'



#############################
'''
REDUCTION METHOD
	possibilities:

	The aditional parameters must be added with the same name
	as in the original function plus the prefix 'RED_'.
	Example:
		if REDUCTION_METHOD is 'pca', the parameter
		n_components must be declared as 
			RED_n_components= ...
'''
#############################
REDUCTION_METHOD	= 'pca'


#############################
'''
CLUSTERING METHOD
	possibilities:
		-MeanShift
		-KMeans
	The aditional parameters must be added with the same name
	as in the original function plus the prefix 'CL_'
	Example:
		if CLUSTERING_METHOD is 'MeanShift', the parameter 
		quantile must be declared as 
			CL_quantile= ...

'''
#############################
CLUSTERING_METHOD	= 'MeanShift'
CLUSTERING_METHOD	= 'KMeans'
#CL_n_clusters=3
CLUSTERING_METHOD	= 'AgglomerativeClustering'

CLUSTERING_OUTPUT_EXT	= '.png'
#CLUSTERING_DATA		= '../empca_trained_coeff/coefficients.dat'
