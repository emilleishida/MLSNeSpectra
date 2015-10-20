from time import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
import numpy as np
import os, sys

import numpy as np
from sklearn import metrics
from sklearn import cluster,neighbors
from sklearn import manifold, datasets

import sncolor as myc

# Next line to silence pyflakes. This import is needed.
Axes3D

#n_points = 1000
#X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)


path1 = '../../empca_trained_coeff/sne.dat'
path2='../../empca_trained_coeff/coefficients.dat'

# read data
X = np.loadtxt(path2)
n_points=len(X[:,0])


#'Branch'
sne_name = np.loadtxt(path1,dtype=str)
leg_type='Wang'
color,marks,cm_name = myc.load_colors(sne_name,type=leg_type)
y=color

figdir='figures/' #'plots_' + case + '/'
if not os.path.isdir(figdir):
    os.makedirs(figdir)


drmethods=['Isomap','MDS','TSNE']
cmethods=['KMeans','AffinityPropagation','DBSCAN','AggC']

niter=2000
sniter='2e3'
n_neighbors = 5
n_components = 3 #dimension
n_clusters = len(cm_name['name'])

# Create a graph capturing local connectivity. Larger number of neighbors
# will give more homogeneous clusters to the cost of computation
# time. A very large number of neighbors gives more evenly distributed
# cluster sizes, but may not impose the local manifold structure of
# the data
knn_graph = neighbors.kneighbors_graph(X, 30, include_self=False)

for drname in drmethods:
    for cname in cmethods:

        case = drname+'_vs_'+cname+'_D'+str(n_components)
        
        #get dimension Reduced data
        if drname=='Isomap': Y = manifold.Isomap(n_neighbors, n_components).fit_transform(X)
        if drname=='MDS': Y = manifold.MDS(n_components, max_iter=niter, n_init=1).fit_transform(X)
        if drname=='TSNE': Y = manifold.TSNE(n_components=n_components, learning_rate=100,n_iter=niter,perplexity=5,random_state=0).fit_transform(X)
        
        #plot dimension reduced data
        fig = plt.figure(figsize=(15, 8))
        ax = fig.add_subplot(121, projection='3d', elev=48, azim=134)

        if n_components==3:
            ax.scatter(Y[:, 0], Y[:, 1], Y[:, 2], c=color)
        if n_components==2:
            ax.scatter(Y[:, 0], Y[:, 1], c=color)
        
        plt.title(drname)
        ax.xaxis.set_major_formatter(NullFormatter())
        ax.yaxis.set_major_formatter(NullFormatter())
        ax.zaxis.set_major_formatter(NullFormatter())
        plt.axis('tight')
        ax.set_xlabel('I1')
        ax.set_ylabel('I2')
        ax.set_zlabel('I3')
        plt.legend(cm_name['name'],loc='best') 


        #plot clusters
        if cname=='KMeans':
            est=cluster.KMeans(n_clusters=n_clusters, n_init=1,init='random').fit(X)
            labels = est.labels_
            nout_clusters_=n_clusters
        if cname=='AffinityPropagation':
            est=cluster.AffinityPropagation(preference=-50).fit(X)
            cluster_centers_indices = est.cluster_centers_indices_
            nout_clusters_ = len(cluster_centers_indices)
            labels = est.labels_
        if cname=='DBSCAN':
            # Compute DBSCAN
            est = cluster.DBSCAN(eps=0.3, min_samples=3,algorithm='kd_tree').fit(X)
            # Number of clusters in labels, ignoring noise if present.
            n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
            core_samples_mask = np.zeros_like(est.labels_, dtype=bool)
            core_samples_mask[est.core_sample_indices_] = True
            labels = est.labels_
            # Number of clusters in labels, ignoring noise if present.
            nout_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        if cname=='AggC':
            est=cluster.AgglomerativeClustering(connectivity=knn_graph,n_clusters=n_clusters, affinity='euclidean').fit(X)
            labels = est.labels_
            nout_clusters_=n_clusters

        print('Method Clustering method: %s' % cname)
        print('Estimated number of clusters: %d' % nout_clusters_)
        # print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
        # print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
        # print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
        # print("Adjusted Rand Index: %0.3f"
        #       % metrics.adjusted_rand_score(labels_true, labels))
        # print("Adjusted Mutual Information: %0.3f"
        #       % metrics.adjusted_mutual_info_score(labels_true, labels))
        # print("Silhouette Coefficient: %0.3f"
        #       % metrics.silhouette_score(X, labels))
    
        ax = fig.add_subplot(122, projection='3d', elev=48, azim=134)

        if n_components==3:
            ax.scatter(Y[:, 0], Y[:, 1], Y[:, 2], c=labels.astype(np.float))
        if n_components==2:
            ax.scatter(Y[:, 0], Y[:, 1], c=labels.astype(np.float))
            
        plt.title(cname+': Number of clusters: %d' % nout_clusters_)    
        ax.w_xaxis.set_ticklabels([])
        ax.w_yaxis.set_ticklabels([])
        ax.w_zaxis.set_ticklabels([])
        ax.set_xlabel('I1')
        ax.set_ylabel('I2')
        ax.set_zlabel('I3')


        plt.savefig(figdir+'/plot_'+case+'_'+leg_type+'_niter'+sniter+'.png')

# kmeans_model = KMeans(n_clusters=3, random_state=1).fit(X)
# labels = kmeans_model.labels_
# metrics.silhouette_score(X, labels, metric='euclidean')
