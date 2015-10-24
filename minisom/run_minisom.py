#!/usr/bin/python
import os
import numpy as np
import minisom
from matplotlib import pyplot as pl
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
from scipy import stats
import pandas as pd


file_name = ""

path_data = "/home/at/Desktop/COIN-Git/MLSNeSpectra/"
#path = "/home/at/Desktop/COIN-Git/MLSNeSpectra/R/out_DeepLearning"
path_plots = "./"


nx = 25
ny = 1



#txtname = "results_som_%s_20x20_sig_0.8_learningrate_0.5_%s.pdf"%("deeplearning","200000iter")

#fig1_name = "som_%s_20x20_sig_0.8_learningrate_0.5_%s.pdf"%("deeplearning","200000iter")

#fig2_name = "prototype_som_%s_20x20_sig_0.8_learningrate_0.5_%s.pdf"%("deeplearning","200000iter")

#empca

#txtname = "results_som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.txt"%("empca_out_coeff",nx,ny,"200000iter")

#fig1_name = "som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.pdf"%("empca_out_coeff",nx,ny,"200000iter")

#fig2_name = "prototype_som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.pdf"%("empca_out_coeff",nx,ny,"200000iter")

#deep learning 100-30-10 

#txtname = "results_som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.txt"%("deeplearning-100-30-10",nx,ny,"200000iter")

#fig1_name = "som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.pdf"%("deeplearning-100-30-10",nx,ny,"200000iter")

#fig2_name = "prototype_som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.pdf"%("deeplearning-100-30-10",nx,ny,"200000iter")


#deep learning 100-30-5

#txtname = "results_som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.txt"%("deeplearning-100-30-5",nx,ny,"200000iter")

#fig1_name = "som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.pdf"%("deeplearning-100-30-5",nx,ny,"200000iter")

#fig2_name = "prototype_som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.pdf"%("deeplearning-100-30-5",nx,ny,"200000iter")

txtname = "results_som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.txt"%("deeplearning-100-30-8",nx,ny,"200000iter")

fig1_name = "som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.pdf"%("deeplearning-100-30-8",nx,ny,"200000iter")

fig2_name = "prototype_som_%s_%dx%d_sig_0.8_learningrate_0.5_%s.pdf"%("deeplearning-100-30-8",nx,ny,"200000iter")


niter = 200000



labels = np.loadtxt(os.path.join(path_data,"data_all_types","labels.dat"))



#d = np.loadtxt(os.path.join(path_data,"data_all_types","out_DeepLearning.dat"))
#d = np.loadtxt(os.path.join(path_data,"python","empca","output_coeff.dat"))
#d = np.loadtxt(os.path.join(path_data,"R","out_DeepLearning","derivatives_dl_100_30_10.dat"))
#d = np.loadtxt(os.path.join(path_data,"R","out_DeepLearning","derivatives_dl_100_30_5.dat"))
d = np.loadtxt(os.path.join(path_data,"R","out_DeepLearning","derivatives_dl_100_30_8.dat"))
d = d[labels==1]
ndim,mdim = d.shape
#d = np.loadtxt(os.path.join(path_data,"R","out_DeepLearning","derivatives_dl_100_30_5.dat"))
#d = d[labels==1,:8]
#d = np.loadtxt(os.path.join(path_data,"data_all_types","out_DeepLearning.dat"))



fluxes = np.loadtxt(os.path.join(path_data,"data_all_types","fluxes.dat"))
fluxes = fluxes[labels==1]

spectra_data = pd.read_csv(os.path.join(path_data,"data_all_types","spectra_data.dat"),sep=" ")
spectra_data = spectra_data[spectra_data["at_max_flag"] == 1]
spectra_data.columns = ["SN","zhelio","MJD","epoch","at_max_flag"]

spectra_data.index=range(ndim)




som = minisom.MiniSom(nx,ny,mdim,sigma=0.8,learning_rate=0.5) 
som.train_random(d,niter)




w = [som.winner(iten) for iten in d]

indx_unique = list( set( w ) )   

indx_counts = sorted([(iten[0],iten[1],w.count(iten) )  for iten in indx_unique], key=lambda x: x[-1])

colors = []

for i in range(len(indx_unique)):
    colors.append((np.random.uniform(0,1),np.random.uniform(0,1),np.random.uniform(0,1)))

colors.sort()


	
fig,ax = pl.subplots(nx,ny)

fig.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=0.0,hspace=0.0)

FILE = open(txtname,"w")
FILE.write("Pair\t Nspec\t mean epoch\t epoch std\n")

for i in xrange(nx):
	
	for j in xrange(ny):
		
		
		
		indices = [ k for k in xrange(len(w)) if w[k] == (i,j)]
		
		if len(indices) == 0:
			ax[i,j].set_xticks([])
			ax[i,j].set_yticks([])

			
			pass
		
		elif len(indices) == 1:
			
			#print indices
			f = fluxes[indices,:][0]
			n2 = f.shape[0]
			
			NORM = f[200:301].sum()
			f/=NORM
			epoch = spectra_data["epoch"].values[indices]
			
			epoch_mean = stats.nanmedian(epoch)
			epoch_std = stats.nanstd(epoch)
			
			ax[i,j].plot(f,'k-' )
			ax[i,j].set_xticks([])
			ax[i,j].set_yticks([])
			
		
		else:
			
			f = fluxes[indices]
			epoch = spectra_data["epoch"].values[indices]
			
			#print indices
			#print f
			#print epoch 
	
			n1,n2 = f.shape
	
			#epoch_mean = stats.nanmedian(epoch)
			epoch_mean = stats.nanmean(epoch)
			epoch_std = stats.nanstd(epoch)
			
			for k in xrange(n1):
				NORM = f[k,200:301].sum()
				for kk in xrange(n2):
					f[k,kk]/=NORM
		
	
			ff=np.median(f,axis=0)
	
			CL68 = np.array( [ [ stats.scoreatpercentile(f[:,k],16), stats.scoreatpercentile(f[:,k],16+68)] for k in xrange(n2)] )
			CL95 = np.array( [ [ stats.scoreatpercentile(f[:,k],2.5), stats.scoreatpercentile(f[:,k],97.5)] for k in xrange(n2) ] )
	
	
			ax[i,j].plot(range(n2),ff,'k-' )
		
			ax[i,j].fill_between( range(n2) ,CL68[:,0], CL68[:,1],interpolate=True,facecolor = "red",alpha = 0.4)
			ax[i,j].fill_between( range(n2) , CL95[:,0], CL95[:,1],interpolate= True,facecolor = "blue",alpha = 0.3)
			

			ax[i,j].set_xticks([])
			ax[i,j].set_yticks([])
			
			
		#ax[i,j].annotate('Npsec=%d'%len(indices), xy=(0.0,0.0),xytext=(0.55 ,0.05), fontsize=14, fontweight='bold') 
		print "Pair = (%d,%d)\t Nspec=%d\t epoch mean=%.2f\t epoch std=%.2f"%(i,j,len(indices),epoch_mean,epoch_std)
		FILE.write("(%d,%d)\t %d\t\t\t %.2f\t\t\t %.2f\n"%(i,j,len(indices),epoch_mean,epoch_std) )

FILE.close()



fig.savefig(fig1_name,format = "pdf",dpi = 4000)

fig,ax = pl.subplots(nx,ny)

fig.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=0.0,hspace=0.0)
for i in xrange(nx):
	
	for j in xrange(ny):
		
		ax[i,j].plot(som.weights[i,j,:])
		ax[i,j].set_xticks([])
		ax[i,j].set_yticks([])


fig.savefig(fig2_name,format = "pdf",dpi=4000)

pl.show()






#for iten in indx_counts:
	
#	pl.figure()
	
#	indices = [ i for i in xrange(len(w)) if w[i] == (iten[0],iten[1])]
#	print indices
	
	
#	f = fluxes[indices] 
	
#	n1,n2 = f.shape
	
	
#	for i in xrange(n1):
#		NORM = f[i,200:301].sum()
#		for j in xrange(n2):
#			f[i,j]/=NORM
		
		
	
	
#	ff=np.median(f,axis=0)
	
#	CL68 = np.array( [ [ stats.scoreatpercentile(f[:,i],16), stats.scoreatpercentile(f[:,i],16+68)] for i in xrange(mdim)] )
#	CL95 = np.array( [
#	 [ stats.scoreatpercentile(f[:,i],2.5), stats.scoreatpercentile(f[:,i],97.5)] for i in xrange(mdim) ] )
	
	
#	pl.plot(range(mdim),ff,'k-')
	
	
	
#	pl.fill_between( range(mdim) ,CL68[:,0], CL68[:,1],interpolate=True,facecolor = "red",alpha = 0.4)
#	pl.fill_between( range(mdim) , CL95[:,0], CL95[:,1],interpolate= True,facecolor = "blue",alpha = 0.3)







	
	




















