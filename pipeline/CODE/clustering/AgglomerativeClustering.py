from sklearn.cluster import AgglomerativeClustering


def clustering(data, params):

    # parse parameters

    if len(params) == 0:
        n_clusters = 4
    else:
        n_clusters = params[0]

    # apply Agglomerative Clustering to reduced data

    model = AgglomerativeClustering(n_clusters=n_clusters)
    model.fit(data)

    # Agglomerative Clustering does not give centers of clusters ...

    return [None, model.labels_]
