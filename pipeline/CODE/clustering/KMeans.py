from sklearn.cluster import KMeans


def clustering(data, params):

    # parse arguments

    for item in params:
	exec(item+'='+str(params[item]))

    # apply KMeans to reduced data

    clusters = KMeans(n_clusters=n_clusters, init=init, tol=tol)
    clusters.fit(data)

    return [clusters.cluster_centers_.T, clusters.labels_]
