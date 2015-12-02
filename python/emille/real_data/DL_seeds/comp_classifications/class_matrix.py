import numpy as np


# path to Kmeans labels results
path_seed1 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_1/cl_data/clustering_KMeans_label_5PC_2groups.dat'
path_seed2 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_2/cl_data/clustering_KMeans_label_5PC_2groups.dat'
path_seed50 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_50/cl_data/clustering_KMeans_label_5PC_2groups.dat'
path_seed100 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_100/cl_data/clustering_KMeans_label_5PC_2groups.dat'
path_seed1000 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_1000/cl_data/clustering_KMeans_label_5PC_2groups.dat'
path_seed5000 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_5000/cl_data/clustering_KMeans_label_5PC_2groups.dat'

# path to spectra id
path_id = '../../../../../data_all_types/spectra_data.dat'

path_set = [path_seed1, path_seed2, path_seed50, path_seed100, path_seed1000, path_seed5000]
keys = [1, 2, 50, 100, 1000, 5000]


# read spectra ID
op2 = open(path_id, 'r')
lin2 = op2.readlines()
op2.close()

names_all = [elem.split() for elem in lin2[1:]]
names_max = [(names_all[i][0], names_all[i][3]) for i in xrange(len(names_all)) if names_all[i][-1] == '1']

snid_class = {}
for k in xrange(len(keys)):

    # read kmeans resulta
    op5 = open(path_set[k], 'r')
    lin5 = op5.readlines()
    op5.close()

    kmeans_classes = [float(elem.split()[0]) for elem in lin5]

    if kmeans_classes[18] == 1.0:
        kmeans_final = []
        for item in kmeans_classes:
            if item == 1.0:
                kmeans_final.append(0.0)
            else:
                kmeans_final.append(1.0)
    else:
        kmeans_final = kmeans_classes

    for jj in xrange(len(names_max)):
        if names_max[jj] not in snid_class.keys():
            snid_class[names_max[jj]] = [kmeans_final[jj]]
        else:
            snid_class[names_max[jj]].append(kmeans_final[jj])

    if len(snid_class[names_max[jj]]) == len(keys):
        snid_class[names_max[jj]] = np.array(snid_class[names_max])    

op3 = open('class_seeds_matrix.dat', 'w')
op3.write('snid \t epoch \t ')
for seed in keys:
    op3.write('seed' + str(seed) + ' \t ')
op3.write('\n')
for ll in xrange(len(names_max)):
    op3.write(names_max[ll][0] + ' \t ' + names_max[ll][1] + ' \t ' )
    for kk in xrange(len(keys)):
        op3.write(str(snid_class[names_max[ll]][kk]) + ' \t ')
    op3.write('\n')

op3.close()
