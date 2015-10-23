#####################################################################################
'''
Original data:
	Used for the reduction,
	not needed if doing clusreing only
'''
ORG_DATA			= '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/SN_simulator/simulated_data/3/derivatives.dat'

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
		error_file can be declared as 
			RED_errors_file= ...
                in order to run with weights=1/errors^2. Its default value is
                None, so empca runs without weights
'''
REDUCTION_METHOD	= 'pca'
RED_n_components    = 5

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
CLUSTERING_METHOD	= 'KMeans'

#####################################################################################
'''
CLUSTERING OUTPUT EXTENSIONS
	extension of output plots produced by pylab
'''
PLOT_EXT	= '.png'

#####################################################################################
'''
CLUSTERING INPUT DATA
	add this ONLY if you want to use a external data source for the clustering,
	if you want to use the data from the pipeline leave it commented.
	Be aware that this data will also go into the plotting.
'''
#REDUCED_DATA_EXTERNAL		= '../empca_trained_coeff/coefficients.dat'

#####################################################################################
'''
PLOTTING INPUT DATA
	add this ONLY if you want to use a external data source of the clusters for the plotting,
	if you want to use the data from the pipeline leave it commented.
	You can also add an external file with different label to set different colors
	to the reduced data. The default color scheme is according to each parent cluster.
'''
#CLUSTERS_DATA_EXTERNAL		= '../empca_trained_coeff/coefficients.dat'
#LABELS_DATA_EXTERNAL		= '../empca_trained_coeff/coefficients.dat'
