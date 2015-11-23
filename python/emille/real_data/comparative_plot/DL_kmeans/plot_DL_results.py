import numpy as np
import pylab as plt
from matplotlib.ticker import MaxNLocator


# number of features in DL results
nfeatures = '4'

# path to DL results
path_small_space = '../../../../../R/out_DeepLearning/out_120,100,90,50,30,20,' + nfeatures + ',20,30,50,90,100,120_seed1_dl.dat'

# path to spectra ID
path_id = '../../../../../data_all_types/spectra_data.dat'

# read spectra ID
op2 = open(path_id, 'r')
lin2 = op2.readlines()
op2.close()

names_all = [elem.split() for elem in lin2[1:]]

# read DL results
op1 = open(path_small_space, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

matrix = np.array([[float(item) for item in data1[i]] for i in xrange(len(data1)) if names_all[i][-1]=='1'])

print 'matrix.shape = ' + str(matrix.shape)

# plot only DL results
plt.figure()
plt.suptitle('Pure Deep Learning results', size=36)
plt.subplot(4,4,1)
plt.scatter(matrix[:,0], matrix[:,0], lw='0',marker='o',s=8)
plt.ylabel('feature 1', fontsize=18)
plt.xticks([])
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,5)
plt.scatter(matrix[:,0], matrix[:,1], lw='0',marker='o',s=8)
plt.ylabel('feature 2', fontsize=18)
plt.xticks([])
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,6)
plt.scatter(matrix[:,1], matrix[:,1], lw='0',marker='o',s=8)
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,9)
plt.scatter(matrix[:,0], matrix[:,2], lw='0',marker='o',s=8)
plt.ylabel('feature 3', fontsize=18)
plt.xticks([])
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,10)
plt.scatter(matrix[:,1], matrix[:,2], lw='0',marker='o',s=8)
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,11)
plt.scatter(matrix[:,2], matrix[:,2], lw='0',marker='o',s=8)
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,13)
plt.scatter(matrix[:,0], matrix[:,3], lw='0',marker='o',s=8)
plt.ylabel('feature 4', fontsize=18)
plt.xlabel('feature 1', fontsize=18)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,14)
plt.scatter(matrix[:,1], matrix[:,3], lw='0',marker='o',s=8)
plt.xlabel('feature 2', fontsize=18)
plt.yticks([])
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,15)
plt.scatter(matrix[:,2], matrix[:,3], lw='0',marker='o',s=8)
plt.xlabel('feature 3',fontsize=18)
plt.yticks([])
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,16)
plt.scatter(matrix[:,3], matrix[:,3], lw='0',marker='o',s=8)
plt.xlabel('feature 4', fontsize=18)
plt.yticks([])
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15,hspace=0.0,wspace=0.0)
plt.show()

