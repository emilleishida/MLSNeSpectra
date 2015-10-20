import pandas as pd
import time as time
import numpy as np
from matplotlib import pyplot as plt
pd.__version__
import sys
import SOMPY as SOM
#%matplotlib inline

Data = np.loadtxt("../empca_trained_coeff/coefficients.dat")
print 'Data size: ', Data.shape

msz0 = 50
msz1 = 50

#This is a random data set, but in general it is assumed that you have your own data set as a numpy ndarray 



#Put this if you are updating the sompy codes otherwise simply remove it
reload(sys.modules['SOMPY'])


sm = SOM.SOM('sm', Data, mapsize = [msz0, msz1],norm_method = 'var',initmethod='pca')
sm.train(n_job = 1, shared_memory = 'no',verbose='final')

sm.view_map(text_size=7)
plt.show()
