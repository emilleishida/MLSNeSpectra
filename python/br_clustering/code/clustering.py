from __future__ import print_function

from time import time
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift,estimate_bandwidth

import argparse
parser = argparse.ArgumentParser()
parser.add_argument( '-nd'	, '--no_diag'	, dest='use_diag'	, default=True		, action='store_false'	, help='do not plot diagonal' )
parser.add_argument( '-nf'	, '--no_fit'	, dest='fit_all'	, default=True		, action='store_false'	, help='do not fit in all dimensions simultanniously' )
parser.add_argument( '-fi'	, '--fit_ind'	, dest='fit_ind'	, default=False		, action='store_true'	, help='fit in each 2 dimensions per time' )
parser.add_argument( '-c'	, '--custering'	, dest='clustering'	, default='MeanShift'	, 			  help='change the clustering method ( possibilities:[MeanShift (default), KMeans] )' )
use_diag	= parser.parse_args().use_diag
fit_all		= parser.parse_args().fit_all
fit_ind		= parser.parse_args().fit_ind
clustering	= parser.parse_args().clustering


from config import *


def do_km(dat,n_init=10):
	if clustering=='MeanShift'	: clusters = MeanShift(bandwidth=estimate_bandwidth(dat,quantile=.25))
	elif clustering=='KMeans'	: clusters = KMeans( n_clusters=N_CLUSTERS, n_init=n_init)
	else: print('<< ',clustering,' >> is an invalid clustering method!');exit()
	clusters.fit(dat)
	return clusters

def ind(i):
	if use_diag: return i
	else:	return i+1


data=np.loadtxt(DATA).T
Ndat=len(data)

if fit_ind:	
	km_ind=[[[] for j in range(Ndat)  ] for i in range(Ndat)]
	for i in range(Ndat):
		for j in range(i+1):
			km_ind[i][j]=do_km( np.array([data[j],data[i]]).T )
km_all=[]
colors='r'
if fit_all:
	km_all 		= do_km(data.T)
	centers_all	= km_all.cluster_centers_.T
	colors		= km_all.labels_.astype(np.float)


Nplt=Ndat-1
if use_diag: Nplt+=1
f,plts  = plt.subplots(Nplt,Nplt,sharex=True,sharey=True)
for i in range(Nplt):
	for j in range(Nplt):
		PLT	= plts[i][j]
		plt.setp( PLT.get_xticklabels(), rotation=45)
		plt.setp( PLT.get_yticklabels(), rotation=45)
		if j>i: PLT.axis('off')
		else:
			dat	= np.array([data[j],data[ind(i)]])
			if fit_ind and fit_all==False:colors = km_ind[ind(i)][j].labels_.astype(np.float)
			PLT.scatter(dat[0],dat[1],c=colors,marker='o',label='data',lw=0)
			if i!=j or (use_diag==False):
				if fit_all: PLT.scatter(centers_all[j],centers_all[ind(i)],c='m',label='cluster centers',marker='x')
				if fit_ind:
					centers=km_ind[ind(i)][j].cluster_centers_.T
					PLT.scatter(centers[0],centers[1],color='c',label='cluster centers',marker='x',linewidths=1)

#plt.legend()
#plt.setp(ax.get_xticklabels(), rotation=-30)
for j in range(Nplt):	plts[Nplt-1][j].set_xlabel('$PC_'+str(j+1)+'$')
for i in range(Nplt):	plts[i][0].set_ylabel('$PC_'+str(ind(i+1))+'$')
plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15)
plt.savefig('clustering_'+clustering+'.pdf')
