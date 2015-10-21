from sklearn.cluster import KMeans


def clustering(data, params):

    # parse arguments

    if len(params) == 0:
        n_clusters = 4
    else:
        n_clusters = params[0]

    # apply KMeans to reduced data

    clusters = KMeans(n_clusters=n_clusters, init='k-means++')
    clusters.fit(data)

    return [clusters.cluster_centers_.T, clusters.labels_]
