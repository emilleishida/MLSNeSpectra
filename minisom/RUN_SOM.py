#!/usr/bin/python
import os,sys
import numpy as np
import minisom
from matplotlib import pyplot as pl
from scipy import stats
import pandas as pd



path = "/home/at/Desktop/COIN-Git/MLSNeSpectra/"



class RUN_SOM:
	
	
	def __init__(self,p):
		self.p = p
	
		
	
		self.folder = os.path.join(self.p["path_out"],self.p["folder_out"])
		if not os.path.exists(self.folder):
		
			os.mkdir(self.folder)
	
		else:
		
			print "Folder %s already exists!"%(self.folder)
	
	
	
	def load_data(self):
		
		self.labels = np.loadtxt(os.path.join(path,"data_all_types","labels.dat"))
	
		self.fluxes = np.loadtxt(os.path.join(path,"data_all_types","fluxes.dat"))		
			
		self.data_all = np.loadtxt(os.path.join(self.p["path_data"],self.p["data_file"]))
		
		self.spectra_data = pd.read_csv(os.path.join(path,"data_all_types","spectra_data.dat"),sep=" ")
	
	
	def select_data(self,SNIa_at_max="Yes"):
		
		if (SNIa_at_max == "Yes"):
		
			self.data = self.data_all[self.labels==1]
			
			ndim = self.data.shape[0]
		
			self.fluxes = self.fluxes[self.labels==1]
			
			self.spectra_data = self.spectra_data[self.spectra_data["at_max_flag"] == 1]
			
			self.spectra_data.columns = ["SN","zhelio","MJD","epoch","at_max_flag"]
			
			self.spectra_data.index=range(ndim)
		
		else:
			
			self.data = self.data_all
		
	
	
	def set_som(self,nx=5,ny=5,Nf=None, sigma = 0.5,learn_rate=0.5):
		
		if Nf is None:
		
			Nf = self.data.shape[1]
		
		
		self.som = minisom.MiniSom(nx,ny,Nf,sigma,learn_rate)
		
		
		
	def set_weights(self,path=None,w = None):
		
		if path is None:
				
			self.som.weights = w
		
		else:
			
			w = np.load(path)["arr_0"]	
			
			if w.shape == (self.som.nx,self.som.ny):
				self.som.weights = w
			
			else:
				
				print "Weights do not have the same shape as the input data!"
				sys.exit()
		
		
	
	
	def run_som(self,Niter=1000,som_type = "random"):
		
		if som_type == "random":
		
			self.som.train_random(self.data,Niter)
	
		elif som_type == "batch":
		
			self.som.train_batch(self.data,Niter )
		
	
	
	
	def get_weights(self):
		
		return self.som.weights
	
	
	
	def analysis(self,file_name):
	
		nx = self.som.neigx.shape[0]
		ny = self.som.neigy.shape[0]
		
		w = [self.som.winner(iten) for iten in self.data]
		indx_unique = list( set( w ) ) 
		
		indx_counts = sorted([(iten[0],iten[1],w.count(iten) )  for iten in indx_unique], key=lambda x: x[-1])

		colors = []

		for i in range(len(indx_unique)):
		
			colors.append((np.random.uniform(0,1),np.random.uniform(0,1),np.random.uniform(0,1)))

		colors.sort()
		
		
		fig,ax = pl.subplots(nx,ny)

		fig.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=0.0,hspace=0.0)

		FILE = open(os.path.join(self.folder,file_name+"_stats.dat"),"w")
		FILE.write("Pair\t Nspec\t mean epoch\t epoch std\n")
		
		# make plots
		
		for i in xrange(nx):
	
			for j in xrange(ny):
		
		
		
				indices = [ k for k in xrange(len(w)) if w[k] == (i,j)]
		
				if len(indices) == 0:
					ax[i,j].set_xticks([])
					ax[i,j].set_yticks([])

			
					pass
		
				elif len(indices) == 1:
			
					#print indices
					f = self.fluxes[indices,:][0]
					n2 = f.shape[0]
			
					NORM = f[200:301].sum()
					f/=NORM
					epoch = self.spectra_data["epoch"].values[indices]
			
					epoch_mean = stats.nanmedian(epoch)
					epoch_std = stats.nanstd(epoch)
			
					ax[i,j].plot(f,'k-' )
					ax[i,j].set_xticks([])
					ax[i,j].set_yticks([])
			
		
				else:
			
					f = self.fluxes[indices]
					epoch = self.spectra_data["epoch"].values[indices]
			
					n1,n2 = f.shape
	
					epoch_mean = stats.nanmedian(epoch)
					#epoch_mean = stats.nanmean(epoch)
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
		
			
		
					print "Pair = (%d,%d)\t Nspec=%d\t epoch mean=%.2f\t epoch std=%.2f"%(i,j,len(indices),epoch_mean,epoch_std)
					FILE.write("(%d,%d)\t %d\t\t\t %.2f\t\t\t %.2f\n"%(i,j,len(indices),epoch_mean,epoch_std) )

		FILE.close()



		fig.savefig(os.path.join(self.folder,file_name+"_grid_plot.pdf"),format = "pdf",dpi = 4000)
	
	
	
	
	
	

		
		
	
	
if __name__ == "__main__":	

	p_in = {"path_data":"/home/at/Desktop/COIN-Git/MLSNeSpectra/R/out_DeepLearning",
			"data_file":"out_120,100,90,50,30,20,9,20,30,50,90,100,120_seed1_dl.dat",
			"folder_out":"results_120,100,90,50,30,20,9,20,30,50,90,100,120_seed1_dl",
			"path_out":"/home/at/Desktop/COIN-Git/MLSNeSpectra/minisom"
			}

		
	SOM = RUN_SOM(p_in)
	
	SOM.load_data()
	
	SOM.select_data(SNIa_at_max="Yes")
		
	SOM.set_som(nx=5,ny=5, sigma =5/2.*(1.-0.1),learn_rate=0.5)
	
	SOM.run_som(Niter = 1000000,som_type = "random")
	
	SOM.analysis("120,100,90,50,30,20,9,20,30,50,90,100,120_seed1_dl_teste_grid_5_sig10perc_learn0.5_niter1000000")
	
	#w = SOM.get_weights()
	#sig = SOM.som._decay_function(SOM.som.sigma,1e4,1e4)
	#learning_rate= SOM.som._decay_function(SOM.som.learning_rate,1e4,1e4)
	
	#print w[0].T
	#print sig,learning_rate
	
	#for i in xrange(10):
		
	#	SOM.set_som(nx=5,ny=5, sigma =  sig,learn_rate=learning_rate)
	#	SOM.set_weights(w=w)
	#	SOM.run_som(Niter = 1000,som_type = "random")
	#	SOM.analysis("120,100,90,50,30,20,4,20,30,50,90,100,120_seed1_dl_teste_grid_5_sig10perc_learn0.5_niter1000"+"_"+str(i))
		
	#	w = SOM.get_weights()
	#	sig = SOM.som._decay_function(SOM.som.sigma,1e3,1e3/2)
	#	learning_rate= SOM.som._decay_function(SOM.som.learning_rate,1e3,1e3/2)
		
	#	print w[0].T
	#	print sig,learning_rate
		
	
		
		
		
		
		











	
	




















