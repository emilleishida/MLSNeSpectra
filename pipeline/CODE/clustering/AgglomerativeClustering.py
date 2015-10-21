from sklearn.cluster import AgglomerativeClustering
from numpy import mean, array


def clustering(data, params):

    # parse parameters

    if len(params) == 0:
        n_clusters = 4
    else:
        n_clusters = params[0]

    # apply Agglomerative Clustering to reduced data

    model = AgglomerativeClustering(n_clusters=n_clusters)
    model.fit(data)

    # Agglomerative Clustering does not give centers of clusters
    # so lets try the mean of each cluster

    centers = []
    for i in range(n_clusters):
        mask = (model.labels_ == i)
        centers.append(mean(data[mask], axis=0))
    centers = array(centers)

    return [centers, model.labels_]
