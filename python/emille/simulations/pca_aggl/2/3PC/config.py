
#####################################################################################
'''
Original data:
	Used for the reduction,
	not needed if doing clusreing only
'''
ORG_DATA			= '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/SN_simulator/simulated_data/2/derivatives.dat'

#####################################################################################
'''
REDUCTION METHOD
	possibilities:
		-pca
	The aditional parameters must be added with the same name
	as in the original function plus the prefix REDUCTION_METHOD'_'.
	Example:
		if REDUCTION_METHOD is 'pca', the parameter
		n_components must be declared as 
			pca_n_components= ...
		if REDUCTION_METHOD is 'empca', the parameter
		error_file can be declared as 
			empca_errors_file= ...
                in order to run with weights=1/errors^2. Its default value is
                None, so empca runs without weights
'''
REDUCTION_METHOD	= 'pca'
pca_n_components = 3

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
	as in the original function plus the prefix CLUSTERING_METHOD'_'
	Example:
		if CLUSTERING_METHOD is 'MeanShift', the parameter 
		quantile must be declared as 
			MeanShift_quantile= ...

'''
CLUSTERING_METHOD	= 'AgglomerativeClustering'
AgglomerativeClustering_n_clusters	= 8

#####################################################################################
'''
CLUSTERING OUTPUT EXTENSIONS
	extension of output plots produced by pylab
'''
PLOT_EXT	= '.png'
PLOT_SPEC_EXT = '.png'

#####################################################################################
'''
QUALITY TEST METHODS
	put one or more (as a vector) quality checks for clustering. possibilities are:
		-silhouette_index
		-Dunn_index
		-DavisBouldin_index
		-vrc

'''
QUALITY_METHODS=['silhouette_index','Dunn_index','DavisBouldin_index','vrc']

#####################################################################################
'''
CLUSTERING INPUT DATA
	add this ONLY if you want to use a external data source for the clustering,
	if you want to use the data from the pipeline leave it commented.
	Be aware that this data will also go into the plotting.
'''

#REDUCED_DATA_EXTERNAL = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/R/out_DeepLearning/out_120,100,90,50,30,20,3,20,30,50,90,100,120_dl.dat'    
#MASK_DATA   = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/data_all_types/labels.dat'
#SPECTRAL_DATA_EXTERNAL      = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/data_all_types/fluxes.dat'

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

