from sklearn.metrics import silhouette_score


def quality(data_red, cluster_centers, labels, params):

    # parse arguments

    for item in params:
        if isinstance(params[item], str):
            exec(item+'='+'"'+params[item]+'"')
        else:
            exec(item+'='+str(params[item]))

    return silhouette_score(data_red, labels, metric=metric)
