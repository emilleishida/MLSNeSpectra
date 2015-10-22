# Explicit configurations of the config file
## Original data:
Used for the reduction, not needed if doing clusreing only

	ORG_DATA	= 'path/data.dat'

## Reduction Method
The key **REDUCTION_METHOD** should be a string with the method name.
For each method you can add extra keys already defined by the method
with the original key name plus the prefix 'RED_'.

Below are the possibilities:

### pca
This uses the pca method and the possible extra keys are

	RED_n_components = int (default=6)

### empca
This uses the empca method and the possible extra keys are

	RED_data_errors_file = **[to be completed]** (default=None)
	RED_n_components = int (default=6)	
	RED_smooth = int (default=0)	
	RED_n_iter	        = int (default=50)	

# Clustering Method
The key **CLUSTERING_METHOD** should be a string with the method name.
For each method you can add extra keys already defined by the method
with the original key name plus the prefix 'CL_'.

Below are the possibilities:

### MeanShift

	CL_quantile = float (default=.25)
	CL_cluster_all = [**to be completed**] (default=True)


### KMeans

	CL_n_clusters = [**to be completed**] (default=4)
	CL_tol = [**to be completed**] (default=1e-4)
	CL_init = [**to be completed**] (default='k-means++')
	CL_n_jobs = [**to be completed**] (default=1)


### AgglomerativeClustering

	CL_n_clusters = [**to be completed**] (default=6)
	CL_affinity = [**to be completed**] (default='euclidean')
	CL_linkage = [**to be completed**] (default='ward')


### AffinityPropagation

	CL_preference = [**to be completed**] (default=None)
	CL_convergence_iter = [**to be completed**] (default=15)
	CL_max_iter = [**to be completed**] (default=200)
	CL_damping = [**to be completed**] (default=0.5)
	CL_affinity = [**to be completed**] (default='euclidean')


### DBSCAN

	CL_eps		= [**to be completed**] (default=0.5)
	CL_min_samples	= [**to be completed**] (default=5)
	CL_metric	= [**to be completed**] (default='euclidean')
	CL_algorithm	= [**to be completed**] (default='auto')
	CL_leaf_size	= [**to be completed**] (default=30)



## Clustering output extension
	Extension of output plots produced by pylab, should be a string.

## Clustering input data
Add this ONLY if you want to use a external data source for the clustering,
if you want to use the data from the pipeline leave it commented

	CLUSTERING_DATA		= 'path/rediced_data.dat'
