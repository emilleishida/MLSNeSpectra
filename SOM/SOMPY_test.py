import pandas as pd
import time as time
import numpy as np
from matplotlib import pyplot as plt
pd.__version__
import sys
import SOMPY as SOM
#%matplotlib inline
import sys
import os


#index = np.arange(0,7,1)
index = [0]
msz0 = 10
msz1 = 10

Path_SOM = "/home/at/Desktop/COIN-Git/MLSNeSpectra/SOM"

path = "../python/SN_simulator/simulated_data"



for iten in index:

    folder = os.path.join(Path_SOM,"sim"+str(iten) )

    if not os.path.exists ( folder ):

        os.mkdir(folder)

    else:
        print "Folder %s already exists!"%folder

        

    Data = np.loadtxt(os.path.join(path,str(iten), "derivatives.dat"  ) )

    n = Data.shape[1]
    print 'Data size: ', Data.shape
     

    reload(sys.modules['SOMPY'])

    sm = SOM.SOM('sm', Data, mapsize = [msz0, msz1],norm_method = 'var',initmethod='pca')
    sm.train(n_job = 1, shared_memory = 'no',verbose='final')

    for i in xrange(n):

        #plt.figure(i)
        sm.view_map(which_dim=i,text_size=7)
        plt.savefig( os.path.join( folder,"variable_"+str(i) ) )

    pl.close("all")
        
        



#sm.view_map(text_size=7)
#plt.show()


    

#Data = np.loadtxt("../empca_trained_coeff/coefficients.dat")

#Data = np.loadtxt("../python/SN_simulator/simulated_data/0/derivatives.dat")

#print 'Data size: ', Data.shape



#This is a random data set, but in general it is assumed that you have your own data set as a numpy ndarray 



#Put this if you are updating the sompy codes otherwise simply remove it
#reload(sys.modules['SOMPY'])


#sm = SOM.SOM('sm', Data, mapsize = [msz0, msz1],norm_method = 'var',initmethod='pca')
#sm.train(n_job = 1, shared_memory = 'no',verbose='final')

#sm.view_map(text_size=7)
#plt.show()
