from sklearn.metrics import *
import numpy as np


def quality(X, cluster_centers, cluster_labels, params):

        # parse arguments

        for item in params:
                if isinstance(params[item], str):
                        exec(item+'='+'"'+params[item]+'"')
                else:
                        exec(item+'='+str(params[item]))

        # numbers of clusters and samples
    
        n_clusters = len(np.unique(cluster_labels))
        n_samples = len(X.shape[0])

        # over-all between-cluster variance

        mean = np.mean(X, axis=0)  # over-all mean
        squared_dist = np.square(pairwise_distances(cluster_centers, mean,
                                                    metric=metric))
        nelements = [np.sum((cluster_labels == i)) for i in
                     range(cluster_centers.shape[0])]
        var_B = np.sum(nelements*dcm2)

        # over-all within-cluster variance

        sum = 0.0
        for i in range(n_clusters):
            mask = (labels == i)
            elements = X[mask]
            squared_dist = np.square(pairwise_distances(elements,
                                                        cluster_centers[i]),
                                     metric=metric)
            sum += np.sum(squared_dist)
        var_W = sum

        # normalization factor

        factor = (n_samples - n_clusters) / (n_clusters - 1)

        return factor * var_B / var_W
