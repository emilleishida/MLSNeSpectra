import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import KernelPCA


path1 = '../../data/derivatives.dat'
case = 'high_SNR'
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


for i in xrange(3):
    for j in xrange(i + 1, 4):
        plt.figure()
        plt.title('gamma = ' + str(par_gamma))
        plt.scatter(X_kpca[:,i], X_kpca[:,j])
        plt.xlabel('kPC' + str(i + 1))
        plt.ylabel('kPC' + str(j + 1))
        plt.savefig('plots/kpca_plot_' + str(i + 1)+ '_' + str(j + 1) + '_gamma_' + str(par_gamma) + '_' + case + '.png')
        
        
plt.figure()
plt.scatter(range(1, 11), kpca.lambdas_[:10]/sum(kpca.lambdas_))
plt.xlabel('kPCA')
plt.ylabel('variance')
plt.savefig('plots/kpca_variance_' + str(par_gamma) + case + '.png')
