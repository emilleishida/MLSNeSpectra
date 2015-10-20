from __future__ import print_function

from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift,estimate_bandwidth


def func(data,pars):
	print ()
	if len(pars)==0: clusters=MeanShift()
	else:
		quantile=pars[0]
		clusters = MeanShift(bandwidth=estimate_bandwidth(data,quantile=quantile))
	clusters.fit(data)
	return clusters.cluster_centers_.T , clusters.labels_
