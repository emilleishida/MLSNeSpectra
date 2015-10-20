import numpy as np
import matplotlib.pyplot as plt
import os,sys

from sklearn.decomposition import KernelPCA
import scipy.cluster.hierarchy as hac
from sklearn.manifold import TSNE

import sncolor as myc
#sys.path.append(os.path.join(os.path.dirname(__file__), '../lle'))

path1 = '../../empca_trained_coeff/sne.dat'
path2='../../empca_trained_coeff/coefficients.dat'
case = 'tsne'



# read data
X_empca = np.loadtxt(path2)

sniter='2e4'
model = TSNE(n_components=2, learning_rate=100,n_iter=20000,perplexity=5,random_state=0)
X_tsne = model.fit_transform(X_empca)

sne_name = np.loadtxt(path1,dtype=str)

#'Branch'
leg_type='Wang'
cols,marks,cm_name = myc.load_colors(sne_name,type=leg_type)

figdir='figures/' #'plots_' + case + '/'
if not os.path.isdir(figdir):
    os.makedirs(figdir)


    
plt.figure()
plt.title('PCS from EMPCA projected by TSNE')
for _s, c, _x, _y in zip(marks, cols, X_tsne[:,0], X_tsne[:,1]):
    plt.scatter(_x, _y, marker=_s, c=c,s=10)

plt.legend(cm_name['name'],loc='best') 

#plt.show()
#plt.xlabel('x' + str(i + 1))
#plt.ylabel('y' + str(j + 1))
plt.savefig(figdir+'/plot_'+case+'_'+leg_type+'_niter'+sniter+'.png')
        
        



