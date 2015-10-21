from sklearn.decomposition.pca import PCA


def reduction(data, params):

    # parse parameters

    for item in params:
	exec(item+'='+str(params[item]))

    # apply PCA

    pca = PCA(n_components=n_components)
    pca.fit(data)
    X = pca.transform(data)

    return X
