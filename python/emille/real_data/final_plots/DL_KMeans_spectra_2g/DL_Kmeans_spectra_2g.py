import pylab as plt
import numpy as np


# path to DL results
path_small_space = '../../../../../R/out_DeepLearning/out_120,100,90,50,30,20,4,20,30,50,90,100,120_seed1_dl.dat'

# path to spectra ID
path_id = '../../../../../data_all_types/spectra_data.dat'

# path to original spectra
path_spectra = '../../../../../data_all_types/fluxes.dat'

# path to kmeans result 4 groups
path_kmeans_2g = '../../DL_kmeans/cl_data_all/clustering_KMeans_label_4PC_2groups.dat'

# read kmeans result 4 groups
op5 = open(path_kmeans_2g, 'r')
lin5 = op5.readlines()
op5.close()

kmeans_classes = [float(elem.split()[0]) for elem in lin5]


# read original spectra
op4 = open(path_spectra, 'r')
lin4 = op4.readlines()
op4.close()

data4 = [elem.split() for elem in lin4]

data_spectra = np.array([[float(item) for item in line] for line in data4])

# read spectra ID
op2 = open(path_id, 'r')
lin2 = op2.readlines()
op2.close()

names_all = [elem.split() for elem in lin2[1:]]
names_max = [names_all[i][0] for i in xrange(len(names_all)) if names_all[i][-1] == '1']



# separate groups according to kmeans classification 4 groups
groups_kmeans = []
for item in [0.0,1.0]:
    kmeans_temp = []
    cont = 0
    for j in xrange(len(data_spectra)):
        if names_all[j][-1] == '1':
            cont = cont + 1
            if kmeans_classes[cont - 1] == item:
                kmeans_temp.append(data_spectra[j])

    groups_kmeans.append(np.array(kmeans_temp))

group_kmeans = np.array(groups_kmeans)
kmeans_rep = [np.array([np.mean(group_kmeans[ll][:,jj]) for jj in xrange(len(data_spectra[0]))]) for ll in xrange(len(groups_kmeans))]
kmeans_std = [np.array([np.std(group_kmeans[ll][:,jj]) for jj in xrange(len(data_spectra[0]))]) for ll in xrange(len(groups_kmeans))]
xaxes = [4000 + 10*ll for ll in xrange(len(data_spectra[0]))]

# plot wang and kmeans results
fig2 = plt.figure(figsize=(18,12))
ax = plt.subplot(111)
ax.fill_between(xaxes, kmeans_rep[0] - kmeans_std[0] + 0.75, kmeans_rep[0] + kmeans_std[0] + 0.75, facecolor='gray', alpha=0.3, label='1$\sigma$')
ax.fill_between(xaxes, kmeans_rep[1] - kmeans_std[1], kmeans_rep[1] + kmeans_std[1], facecolor='gray', alpha=0.3)
line, = ax.plot(xaxes, kmeans_rep[0] + 0.75, color='green',lw=4.0, label='DL+KM G1')
line, = ax.plot(xaxes, kmeans_rep[1], lw=4.0, color='red', label='DL+KM G2')

plt.xlabel('wavelength ($\AA$)', fontsize=26)
plt.ylabel('flux (arbitrary units)', fontsize=26)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.tight_layout()
plt.ylim(0, 2.0)
ax.legend(loc='upper center', bbox_to_anchor=(0.9, 1.016), ncol=1, fontsize=26)
plt.savefig("DL_KMeans_spectra_2g.pdf", format='pdf',dpi=1000)
plt.close()


