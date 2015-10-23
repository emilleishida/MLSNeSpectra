from sklearn.metrics import silhouette_score


def quality(data_red, cluster_centers, labels):

    return silhouette_score(data_red, labels)
