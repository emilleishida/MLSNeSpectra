from sklearn.cluster import KMeans


def clustering(data, params):

    # parse arguments

    n_clusters = params.n_clusters
    tol = params.tol

    # apply KMeans to reduced data

    clusters = KMeans(n_clusters=n_clusters, init='k-means++', tol=tol)
    clusters.fit(data)

    return [clusters.cluster_centers_.T, clusters.labels_]
