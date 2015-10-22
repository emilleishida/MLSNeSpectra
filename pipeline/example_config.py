#####################################################################################
'''
Original data:
	Used for the reduction,
	not needed if doing clusreing only
'''
ORG_DATA			= '../data/derivatives.dat'

#####################################################################################
'''
REDUCTION METHOD
	possibilities:
		-pca
	The aditional parameters must be added with the same name
	as in the original function plus the prefix 'RED_'.
	Example:
		if REDUCTION_METHOD is 'pca', the parameter
		n_components must be declared as 
			RED_n_components= ...
		if REDUCTION_METHOD is 'empca', the parameter
		error_file can be declared must be declared as 
			RED_errors_file ...
                in order to run with weights=1/errors^2, default is None, so
                empca run without weights
'''
REDUCTION_METHOD	= 'pca'

#####################################################################################
'''
CLUSTERING METHOD
	possibilities:
		-MeanShift
		-KMeans
		-AffinityPropagation
		-AgglomerativeClustering
		-DBSCAN

	The aditional parameters must be added with the same name
	as in the original function plus the prefix 'CL_'
	Example:
		if CLUSTERING_METHOD is 'MeanShift', the parameter 
		quantile must be declared as 
			CL_quantile= ...

'''
CLUSTERING_METHOD	= 'MeanShift'

#####################################################################################
'''
CLUSTERING OUTPUT EXTENSIONS
	extension of output plots produced by pylab
'''
CLUSTERING_OUTPUT_EXT	= '.png'

#####################################################################################
'''
CLUSTERING INPUT DATA
	add this ONLY if you want to use a external data source for the clustering,
	if you want to use the data from the pipeline leave it commented
'''
#CLUSTERING_DATA		= '../empca_trained_coeff/coefficients.dat'
