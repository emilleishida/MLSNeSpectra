import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import KernelPCA


path1 = '../../data/derivatives.dat'
par_gamma = 10.0

# read data
op1 = open(path1, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

# build matrix
matrix = np.array([[float(item) for item in line] for line in data1[1:]])

# perform kpca
kpca = KernelPCA(kernel="rbf", gamma=par_gamma)
X_kpca = kpca.fit_transform(matrix)


plt.figure()
plt.title('gamma = ' + str(par_gamma))
plt.scatter(X_kpca[:,0], X_kpca[:,1])
plt.xlabel('kPC1')
plt.ylabel('kPC2')
plt.savefig('plots/kpca_plot_1_2_gamma_' + str(par_gamma) + '.png')

plt.figure()
plt.title('gamma = ' + str(par_gamma))
plt.scatter(X_kpca[:,0], X_kpca[:,2])
plt.xlabel('kPC1')
plt.ylabel('kPC3')
plt.savefig('plots/kpca_plot_1_3_gamma_' + str(par_gamma) + '.png')

plt.figure()
plt.title('gamma = ' + str(par_gamma))
plt.scatter(X_kpca[:,0], X_kpca[:,3])
plt.xlabel('kPC1')
plt.ylabel('kPC3')
plt.savefig('plots/kpca_plot_1_4_gamma_' + str(par_gamma) + '.png')

plt.figure()
plt.title('gamma = ' + str(par_gamma))
plt.scatter(X_kpca[:,1], X_kpca[:,2])
plt.xlabel('kPC1')
plt.ylabel('kPC3')
plt.savefig('plots/kpca_plot_2_3_gamma_' + str(par_gamma) + '.png')

plt.figure()
plt.title('gamma = ' + str(par_gamma))
plt.scatter(X_kpca[:,1], X_kpca[:,3])
plt.xlabel('kPC1')
plt.ylabel('kPC4')
plt.savefig('plots/kpca_plot_2_4_gamma_' + str(par_gamma) + '.png')

plt.figure()
plt.title('gamma = ' + str(par_gamma))
plt.scatter(X_kpca[:,2], X_kpca[:,3])
plt.xlabel('kPC1')
plt.ylabel('kPC3')
plt.savefig('kpca_plot_3_4_gamma_' + str(par_gamma) + '.png')