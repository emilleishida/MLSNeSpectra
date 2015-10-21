from sklearn.decomposition.pca import PCA
from numpy import savetxt


def reduction(data, params):

    # parse parameters

    for item in params:
	exec(item+'='+str(params[item]))

    # apply PCA

    pca = PCA(n_components=n_components)
    pca.fit(data)
    X = pca.transform(data)

    # save output

    fname = './data/' + REDUCTION_METHOD + '_ncomp' + str(n_components) +'.dat'
    savetxt(X.T, fname)

    return fname
