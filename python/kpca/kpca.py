import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.decomposition import KernelPCA
import scipy.cluster.hierarchy as hac
import fastcluster


path1 = '../../data/fake_data.dat'
case = 'fake'
par_gamma = 10.0

# read data
op1 = open(path1, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

# build matrix
matrix = np.array([[float(item) for item in line] for line in data1[1:]])

# perform kpca
kpca = KernelPCA(kernel="linear", gamma=par_gamma)
X_kpca = kpca.fit_transform(matrix)

if not os.path.isdir('plots_' + case + '/'):
    os.makesdirs('plots_' + case + '/')

for i in xrange(0,1):
    for j in xrange(1, 2):
        if i < j:
            plt.figure()
            plt.title('gamma = ' + str(par_gamma))
            plt.scatter(X_kpca[:,i], X_kpca[:,j])
            plt.xlabel('kPC' + str(i + 1))
            plt.ylabel('kPC' + str(j + 1))
            plt.savefig('plots_' + case + '/kpca_plot_' + str(i + 1)+ '_' + str(j + 1) + '_gamma_' + str(par_gamma) + '_' + case + '.png')
        
        
plt.figure()
plt.scatter(range(1, 11), kpca.lambdas_[:10]/sum(kpca.lambdas_))
plt.xlabel('kPCA')
plt.ylabel('variance')
plt.savefig('plots_' + case + '/kpca_variance_' + str(par_gamma) + case + '.png')

"""
# clustering
from sklearn import mixture
cv_types = ['spherical', 'tied', 'diag','full']
color_iter =['k', 'r', 'g', 'b', 'c', 'm', 'y']
data = X_kpca[:,2:4]


ncomp_try = 8
n_components_range = range(1, ncomp_try)

#####################################################################################
yborder = ( min( data[:,1]) - (max( data[:,1])-min( data[:,1]))/5.0, max( data[:,1]) + (max( data[:,1])-min( data[:,1]))/5.0)

lowest_aic = np.infty
lowest_bic = np.infty
aic = []
bic = []

for cv_type in cv_types:
    for n_components in n_components_range:
        # Fit a mixture of Gaussians with EM
        gmm = mixture.GMM(n_components=n_components, covariance_type=cv_type, n_iter=1000)
        gmm.fit( data[:,:-1] )
        aic.append(gmm.aic(data[:,:-1])) 
        bic.append(gmm.bic(data[:,:-1]))   
        if aic[-1] < lowest_aic:
            lowest_aic = aic[-1]
            best_gmm2 = gmm
            bestmodel = cv_type   

        if bic[-1] < lowest_bic:    
            lowest_bic = bic[-1]
            best_bic_gmm2 = gmm
            bestmodel_bic = cv_type

ncomp = best_gmm2.n_components
model = bestmodel 

ncomp_bic = best_bic_gmm2.n_components
model_bic = bestmodel_bic

aic = np.array(aic)
bic = np.array(bic)

clf2 = best_gmm2
clf2_bic = best_bic_gmm2

Y_ = clf2.predict(data[:,:-1])
Y_bic_ = clf2_bic.predict(data[:,:-1])

plt.figure()
plt.subplot(1,2,1)
plt.title('AIC, ncomp = ' + str(ncomp))
splot = plt.gca()
for i, (mean, covar, color) in enumerate(zip(clf2.means_, clf2.covars_,color_iter)):
    #least square fit for groups found
    if not np.any(Y_ == i):
       continue
    splot.scatter(data[Y_ == i, 0], data[Y_ == i, 1], 1.2, color=color)
splot.set_xlabel( 'kPC3', fontsize=15 )
splot.set_ylabel( 'kPC4', fontsize=15)
splot.tick_params(axis='both', which='major', labelsize=10)
splot.invert_yaxis()
splot.set_ylim( yborder[1], yborder[0] )    
plt.subplots_adjust(hspace=.4, bottom=.1, top=0.9)

plt.subplot(1,2,2)
plt.title('BIC, ncomp = ' + str(ncomp_bic))
splot2 = plt.gca()
for i, (mean, covar, color) in enumerate(zip(clf2_bic.means_, clf2_bic.covars_,color_iter)):
    #least square fit for groups found
    if not np.any(Y_bic_ == i):
       continue
    splot2.scatter(data[Y_bic_ == i, 0], data[Y_bic_ == i, 1], 1.2, color=color)
splot2.set_xlabel( 'kPC3', fontsize=15 )
splot2.set_ylabel(  'kPC4', fontsize=15)
splot2.tick_params(axis='both', which='major', labelsize=10)
splot2.invert_yaxis()
splot2.set_ylim( yborder[1], yborder[0] )    
plt.subplots_adjust(hspace=.4, bottom=.1, top=0.9)

plt.show()
"""



