from sklearn.cluster import MeanShift, estimate_bandwidth


def clustering(data, params):

    # parse arguments

    if len(params) == 0:
        quantile = .25
    else:
        quantile = params[0]

    # apply Mean Shift to reduced data

    clusters = MeanShift(bandwidth=estimate_bandwidth(data, quantile=quantile))
    clusters.fit(data)

    return [clusters.cluster_centers_.T, clusters.labels_]
