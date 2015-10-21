from sklearn.cluster import AgglomerativeClustering
from numpy import mean, array


def clustering(data, params):

    # parse parameters

    n_clusters = params.n_clusters
    affinity = params.affinity
    linkage = params.linkage

    # apply Agglomerative Clustering to reduced data

    clusters = AgglomerativeClustering(n_clusters=n_clusters,
                                       affinity=affinity, linkage=linkage)
    clusters.fit(data)

    # Agglomerative Clustering does not give centers of clusters
    # so lets try the mean of each cluster

    cluster_centers = []
    for i in range(n_clusters):
        mask = (clusters.labels_ == i)
        cluster_centers.append(mean(data[mask], axis=0))
    cluster_centers = array(cluster_centers)

    return [cluster_centers.T, clusters.labels_]
