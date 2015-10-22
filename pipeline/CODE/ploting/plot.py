from __future__ import print_function


import numpy as np
from config import REDUCTION_METHOD, CLUSTERING_METHOD 

import argparse
parser = argparse.ArgumentParser()
parser.add_argument( '-nd'	, '--no_diag'	, dest='use_diag'	, default=True		, action='store_false'	, help='do not plot diagonal' )
parser.add_argument( '-nf'	, '--no_fit'	, dest='fit_all'	, default=True		, action='store_false'	, help='do not fit in all dimensions simultanniously' )
parser.add_argument( '-nc'	, '--no_colors'	, dest='do_colors'	, default=True		, action='store_false'	, help='do not use colors' )
parser.add_argument( '-w'	, '--window'	, dest='in_window'	, default=False		, action='store_true'	, help='keep plot in interactive window' )
use_diag	= parser.parse_args().use_diag
fit_all		= parser.parse_args().fit_all
do_colors	= parser.parse_args().do_colors
in_window	= parser.parse_args().in_window

import matplotlib
if in_window==False: matplotlib.use('Agg')
import matplotlib.pyplot as plt

def ind(i):
	if use_diag: return i
	else:	return i+1
def crop(data,i,j):
	return np.array([data[j],data[ind(i)]])
def plot_data(red_data,cl_data,label_data,out_name='plots/plot.png'):
	print('plot')
	Ndat=len(red_data)
	Nplt=Ndat-1
	if use_diag: Nplt+=1
	f,plts  = plt.subplots(Nplt,Nplt,sharex=True,sharey=True,figsize=(16,12))
	colors	= 'r'
	if do_colors and fit_all: colors = label_data.astype(np.float)
	for i in range(Nplt):
		for j in range(Nplt):
			PLT	= plts[i][j]
			plt.setp( PLT.get_xticklabels(), rotation=45)
			plt.setp( PLT.get_yticklabels(), rotation=45)
#			PLT.locator_params('x',nbins=4)
#			PLT.locator_params('y',nbins=4)
			dat	= crop(red_data,i,j)
			cl_dat	= crop(cl_data,i,j)

			if j>i: PLT.axis('off')
			else:
				PLT.scatter(dat[0],dat[1],c=colors,marker='o',label='data',lw=0,s=8)
				if fit_all: PLT.scatter(cl_dat[0],cl_dat[1],c='m',label='cluster centers',marker='x')
	for j in range(Nplt):	plts[Nplt-1][j].set_xlabel('$PC_'+str(j+1)+'$')
	for i in range(Nplt):	plts[i][0].set_ylabel('$PC_'+str(ind(i+1))+'$')
	plts[0][Nplt-1].text(0,0,'REDUCTION_METHOD:\n  '+REDUCTION_METHOD+'\nCLUSTERING_METHOD:\n  '+CLUSTERING_METHOD,bbox={'facecolor':'1.', 'alpha':0.5, 'pad':20})
	plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15,hspace=0,wspace=0)
	if in_window	: plt.show(block=True)
	else		: plt.savefig(out_name)
