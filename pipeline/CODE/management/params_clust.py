from __future__ import print_function
MeanShift_dict=dict([
	[ 'quantile'	, .25	],
	[ 'quantile1'	, .251	],
	[ 'quantile2'	, .225	],
	[ 'quantile3'	, .235	],
])

KMeans_dict=dict([
	[ 'n_clusters'	, 2		],
	[ 'init'	, '"k-means++"'	],
	[ 'tol'		, 1e-4		],
])

AgglomerativeClustering_dict=dict([
	[ 'n_clusters'	, 6		],
	[ 'affinity'	, '"euclidean"'	],
	[ 'linkage'	, '"ward"'	],
])
