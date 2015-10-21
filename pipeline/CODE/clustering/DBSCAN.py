from numpy import mean, array
from sklearn.cluster import DBSCAN


def clustering(data, params):
    
    # parse parameters

    eps = params.eps
    min_samples = params.min_samples
    metric = params.metric
    algorithm = params.algorithm
    leaf_size = params.leaf_size

    # apply DBSCAN to reduced data

    clusters = DBSCAN(eps=eps, min_samples=min_samples, metric=metric,
                      algorithm=algorithm, leaf_size=leaf_size).fit(data)
    labels = clusters.labels_
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

    # DBSCAN does not give centers of clusters
    # so lets try the mean of each cluster

    cluster_centers = []
    for i in range(n_clusters):
        mask = (clusters.labels_ == i)
        cluster_centers.append(mean(data[mask], axis=0))
    cluster_centers = array(cluster_centers)

    return [cluster_centers.T, clusters.labels_]
    
