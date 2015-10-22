from __future__ import print_function

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from config import REDUCTION_METHOD, CLUSTERING_METHOD 

import argparse
parser = argparse.ArgumentParser()
parser.add_argument( '-nd'	, '--no_diag'	, dest='use_diag'	, default=True		, action='store_false'	, help='do not plot diagonal' )
parser.add_argument( '-nf'	, '--no_fit'	, dest='fit_all'	, default=True		, action='store_false'	, help='do not fit in all dimensions simultanniously' )
parser.add_argument( '-fi'	, '--fit_ind'	, dest='fit_ind'	, default=False		, action='store_true'	, help='fit in each 2 dimensions per time' )
use_diag	= parser.parse_args().use_diag
fit_all		= parser.parse_args().fit_all
fit_ind		= parser.parse_args().fit_ind


def ind(i):
	if use_diag: return i
	else:	return i+1
def plot_clustering(cl_func,data,CLUSTERING_OUT_NAME='clustering.png'):
	print('plot_clustering')
	Ndat=len(data)
	if fit_ind:	
		clust_ind=[[[] for j in range(Ndat)  ] for i in range(Ndat)]
		for i in range(Ndat):
			for j in range(i+1): clust_ind[i][j]=cl_func( np.array([data[j],data[i]]).T )
	if fit_all:	clust_all	= cl_func(data.T)
	Nplt=Ndat-1
	if use_diag: Nplt+=1
	f,plts  = plt.subplots(Nplt,Nplt,sharex=True,sharey=True,figsize=(16,12))
	colors	= 'r'
	for i in range(Nplt):
		for j in range(Nplt):
			PLT	= plts[i][j]
			plt.setp( PLT.get_xticklabels(), rotation=45)
			plt.setp( PLT.get_yticklabels(), rotation=45)
#			PLT.locator_params('x',nbins=4)
#			PLT.locator_params('y',nbins=4)
			if j>i: PLT.axis('off')
			else:
				dat	= np.array([data[j],data[ind(i)]])
				if fit_all	: colors = clust_all[1].astype(np.float)
				elif fit_ind	: colors = clust_ind[ind(i)][j][1].astype(np.float)
				PLT.scatter(dat[0],dat[1],c=colors,marker='o',label='data',lw=0,s=8)
				if i!=j or (use_diag==False):
					if fit_all: PLT.scatter(clust_all[0][j],clust_all[0][ind(i)],c='m',label='cluster centers',marker='x')
					if fit_ind:
						centers=clust_ind[ind(i)][j][0]
						PLT.scatter(centers[0],centers[1],color='c',label='cluster centers',marker='x',linewidths=1)
	for j in range(Nplt):	plts[Nplt-1][j].set_xlabel('$PC_'+str(j+1)+'$')
	for i in range(Nplt):	plts[i][0].set_ylabel('$PC_'+str(ind(i+1))+'$')
	plts[0][Nplt-1].text(0,0,'REDUCTION_METHOD:\n  '+REDUCTION_METHOD+'\nCLUSTERING_METHOD:\n  '+CLUSTERING_METHOD,bbox={'facecolor':'1.', 'alpha':0.5, 'pad':20})
	plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15,hspace=0,wspace=0)
	plt.savefig('plots/'+CLUSTERING_OUT_NAME)
