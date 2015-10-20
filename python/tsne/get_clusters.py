from time import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
import numpy as np
import os, sys

import numpy as np
from sklearn.cluster import KMeans
from sklearn import manifold, datasets

import sncolor as myc

# Next line to silence pyflakes. This import is needed.
Axes3D

#n_points = 1000
#X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)

n_neighbors = 5
n_components = 2

path1 = '../../empca_trained_coeff/sne.dat'
path2='../../empca_trained_coeff/coefficients.dat'
case = 'isomap_vs_kmeans'

# read data
X = np.loadtxt(path2)
n_points=len(X[:,0])
sniter='2e4'

#'Branch'
sne_name = np.loadtxt(path1,dtype=str)
leg_type='Wang'
color,marks,cm_name = myc.load_colors(sne_name,type=leg_type)
y=color

figdir='figures/' #'plots_' + case + '/'
if not os.path.isdir(figdir):
    os.makedirs(figdir)


n_neighbors = 5
n_components = 3
Y = manifold.Isomap(n_neighbors, n_components).fit_transform(X)


fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(121, projection='3d', elev=48, azim=134)
ax.scatter(Y[:, 0], Y[:, 1],Y[:,2], c=color)
plt.title("Isomap")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
ax.zaxis.set_major_formatter(NullFormatter())
plt.axis('tight')
ax.set_xlabel('I1')
ax.set_ylabel('I2')
ax.set_zlabel('I3')
plt.legend(cm_name['name'],loc='best') 

#'k_means_iris_3': KMeans(n_clusters=3),
#              'k_means_iris_8': KMeans(n_clusters=8),
              
estimators = {'k_means_iris_bad_init': KMeans(n_clusters=3, n_init=1,
                                              init='random')}


for name, est in estimators.items():
    ax = fig.add_subplot(122, projection='3d', elev=48, azim=134)
    
    est.fit(X)
    labels = est.labels_

    ax.scatter(Y[:, 0], Y[:, 1], Y[:, 2], c=labels.astype(np.float))
    plt.title("KMeans")    
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
