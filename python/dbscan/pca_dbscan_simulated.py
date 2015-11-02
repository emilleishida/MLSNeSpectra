import os
import numpy
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition.pca import PCA
import matplotlib.pyplot as plt

stages = [0,1,2,3,4,5,6]
eps_range = numpy.arange(0.01,2,0.01)

# minimum number of points that must be contained in a cluster
min_samples = 2
n_pca_components = 2

for stage in stages:
    print("Processing stage %i ..." % stage)
    data_dir = '../SN_simulator/simulated_data/' + str(stage)
    for i in xrange(len(eps_range)):

        eps = eps_range[i]

        # data
        derivatives = numpy.loadtxt(os.path.join(data_dir, 'derivatives.dat'))

        # apply PCA + DBSCAN
        pca = PCA(n_components=n_pca_components)
        pca.fit(derivatives)
        X = pca.transform(derivatives)
        X = StandardScaler().fit_transform(X)

        model = DBSCAN(eps=eps, min_samples=min_samples, algorithm='kd_tree')
        model.fit(X)

        # output
        core_samples_mask = numpy.zeros_like(model.labels_, dtype=bool)
        core_samples_mask[model.core_sample_indices_] = True
        labels = model.labels_
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        print('[stage=%i, eps=%f] Number of clusters: %d' % (stage, eps, n_clusters_))

        # plot resuls (ONLY FIRST 2 DIMENSIONS)
        fig, ax = plt.subplots(figsize=(15,15))
        unique_labels = set(labels)
        colors = plt.cm.Spectral(numpy.linspace(0, 1, len(unique_labels)))

        for k, col in zip(unique_labels, colors):

            # noise
            if k == -1:
                col = 'k'

            class_member_mask = (labels == k)

            xy = X[class_member_mask & core_samples_mask]
            ax.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=10, alpha=0.6)

            xy = X[class_member_mask & ~core_samples_mask]
            ax.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor='k', markeredgecolor='k', markersize=4)
            
        plt.title('ONLY 2D PLOT!!!\nEstimated number of clusters [eps=%f]: %d' % (eps, n_clusters_))

        ofile = os.path.join('plots_simulated', "%iD" % n_pca_components, str(stage), str(eps) + "_pca_dbscan_n_clust_%d.png" % n_clusters_)
        if not os.path.exists(os.path.dirname(ofile)):
            os.makedirs(os.path.dirname(ofile))
        plt.savefig(ofile, dpi=40)

