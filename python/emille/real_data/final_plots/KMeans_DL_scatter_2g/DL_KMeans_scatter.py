import pylab as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# path to DL results
path_small_space = '../../../../../R/out_DeepLearning/out_120,100,90,50,30,20,4,20,30,50,90,100,120_seed1_dl.dat'

# path to spectra ID
path_id = '../../../../../data_all_types/spectra_data.dat'

# path to kmeans result
path_kmeans = '../../DL_kmeans/cl_data_all/clustering_KMeans_label_4PC_2groups.dat'

# color for plotting
c = [ 'green', 'red', 'blue', 'orange']

# markers for ploting
mark =  ['^','o',  's', 'd', '*']

# marker size
ss = [60, 40, 40, 60]

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

# read kmeans results
op3 = open(path_kmeans, 'r')
lin3 = op3.readlines()
op3.close()

classes = np.array([float(elem.split()[0]) for elem in lin3])
group1 = classes == 0.0
group2 = classes == 1.0

# plot only DL results
fig = plt.figure(figsize=(20,14))
plt.subplot(4,4,1)
panels = []
panels.append(plt.scatter(matrix[group1,0], matrix[group1,0], lw='0',marker=mark[0],s=ss[0], color=c[0]))
panels.append(plt.scatter(matrix[group2,0], matrix[group2,0], lw='0',marker=mark[1],s=ss[1], color=c[1]))
plt.ylabel('feature 1', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,5)
plt.scatter(matrix[group1,0], matrix[group1,1], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,0], matrix[group2,1], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.ylabel('feature 2', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,6)
plt.scatter(matrix[group1,1], matrix[group1,1], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,1], matrix[group2,1], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.xticks([])
plt.yticks([])

plt.subplot(4,4,9)
plt.scatter(matrix[group1,0], matrix[group1,2], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,0], matrix[group2,2], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.ylabel('feature 3', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,10)
plt.scatter(matrix[group1,1], matrix[group1,2], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,1], matrix[group2,2], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.xticks([])
plt.yticks([])

plt.subplot(4,4,11)
plt.scatter(matrix[group1,2], matrix[group1,2], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,2], matrix[group2,2], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,13)
plt.scatter(matrix[group1,0], matrix[group1,3], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,0], matrix[group2,3], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.ylabel('feature 4', fontsize=26)
plt.xlabel('feature 1', fontsize=26)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)


plt.subplot(4,4,14)
plt.scatter(matrix[group1,1], matrix[group1,3], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,1], matrix[group2,3], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.xlabel('feature 2', fontsize=26)
plt.yticks([])
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xticks(fontsize=22)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,15)
plt.scatter(matrix[group1,2], matrix[group1,3], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,2], matrix[group2,3], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.xlabel('feature 3',fontsize=26)
plt.yticks([])
plt.xticks(fontsize=22)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


plt.subplot(4,4,16)
plt.scatter(matrix[group1,3], matrix[group1,3], lw='0',marker=mark[0],s=ss[0], color=c[0])
plt.scatter(matrix[group2,3], matrix[group2,3], lw='0',marker=mark[1],s=ss[1], color=c[1])
plt.xlabel('feature 4', fontsize=26)
plt.yticks([])
plt.xticks(fontsize=22)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplots_adjust(left=0.075, right=0.975, top=0.975, bottom=0.075,hspace=0.0,wspace=0.0)
legs=fig.legend(panels, ['Group 1', 'Group 2'], loc = (0.770, 0.8535), title='Kmeans classfication', fontsize=26)
plt.setp(legs.get_title(),fontsize=26)
plt.savefig("DL_KMeans_scatter_2g.pdf", format='pdf',dpi=1000)

