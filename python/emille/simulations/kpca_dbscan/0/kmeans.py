import numpy as np
import pylab as plt
import matplotlib.cm as cm

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

path1 = 'red_data/reduced_data_kpca.dat'
nc = 2

pc1 = 0
pc2 = 1
colors = ['#4EACC5', '#FF9C34', '#4E9A06']

# read PCs projections
op1 = open(path1, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

data = np.array([[float(data1[i][j]) for j in xrange(len(data1[0]))] for i in xrange(len(data1))])

# Compute clustering with Means

k_means = KMeans(init='k-means++', n_clusters=nc, n_init=10)
k_means.fit(data)
k_means_labels = k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_
k_means_labels_unique = np.unique(k_means_labels)

plt.figure()
ax = plt.gca()
for k, col in zip(range(nc), colors):
    my_members = k_means_labels == k
    cluster_center = k_means_cluster_centers[k]
    ax.plot(data[my_members, pc1], data[my_members, pc2], 'w',
            markerfacecolor=col, marker='.')
    ax.plot(cluster_center[pc1], cluster_center[pc2], 'o', markerfacecolor=col,
            markeredgecolor='k', markersize=6)
ax.set_xlabel('PC' + str(pc1 + 1))
ax.set_ylabel('PC' + str(pc2 + 1))

plt.show()


range_n_clusters = 10
for n_clusters in xrange(2, range_n_clusters):

    plt.xlim([-0.1, 1])
    # The (n_clusters+1)*10 is for inserting blank space between silhouette
    # plots of individual clusters, to demarcate them clearly.
    plt.ylim([0, len(data) + (n_clusters + 1) * 10])

    # Initialize the clusterer with n_clusters value and a random generator
    # seed of 10 for reproducibility.
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(data)

    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    silhouette_avg = silhouette_score(data, cluster_labels)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)

    # Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(data, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to
        # cluster i, and sort them
        ith_cluster_silhouette_values = \
            sample_silhouette_values[cluster_labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.spectral(float(i) / n_clusters)
        plt.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)

        # Label the silhouette plots with their cluster numbers at the middle
        plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples

    plt.title("The silhouette plot for the various clusters.")
    plt.xlabel("The silhouette coefficient values")
    plt.ylabel("Cluster label")

    # The vertical line for average silhoutte score of all the values
    plt.axvline(x=silhouette_avg, color="red", linestyle="--")

    plt.yticks([])  # Clear the yaxis labels / ticks
    plt.xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # 2nd Plot showing the actual clusters formed
    colors = cm.spectral(cluster_labels.astype(float) / n_clusters)
    plt.scatter(data[:, pc1], data[:, pc2], marker='.', s=30, lw=0, alpha=0.7,
                c=colors)

    # Labeling the clusters
    centers = clusterer.cluster_centers_
    # Draw white circles at cluster centers
    plt.scatter(centers[:, pc1], centers[:, pc2],
                marker='o', c="white", alpha=1, s=200)

    for i, c in enumerate(centers):
        plt.scatter(c[pc1], c[pc2], marker='$%d$' % i, alpha=1, s=50)

    plt.title("The visualization of the clustered data.")
    plt.xlabel("Feature space for the 1st feature")
    plt.ylabel("Feature space for the 2nd feature")

    plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                  "with n_clusters = %d" % n_clusters),
                 fontsize=14, fontweight='bold')

    plt.show()

