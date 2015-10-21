from sklearn.decomposition.pca import PCA


def reduction(data, params):

    # parse parameters

    if len(params) == 0:
        n_components = 6
    else:
        n_components = params[0]

    # apply PCA

    pca = PCA(n_components=n_components)
    pca.fit(data)
    X = pca.transform(data)
    
    return X
