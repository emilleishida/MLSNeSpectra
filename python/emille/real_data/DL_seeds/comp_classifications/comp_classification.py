import numpy as np


# path to Kmeans labels results
path_seed1 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_1/cl_data/clustering_KMeans_label_5PC_2groups.dat'
path_seed2 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_2/cl_data/clustering_KMeans_label_5PC_2groups.dat'
path_seed50 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_50/cl_data/clustering_KMeans_label_5PC_2groups.dat'
path_seed100 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_100/cl_data/clustering_KMeans_label_5PC_2groups.dat'
path_seed1000 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/real_data/DL_seeds/seed_1000/cl_data/clustering_KMeans_label_5PC_2groups.dat'

# path to spectra id
path_id = '../../../../../data_all_types/spectra_data.dat'


seed = 1
ngroups = 2

path_set = [path_seed1, path_seed2, path_seed50, path_seed100, path_seed1000]
keys = [1, 2, 50, 100, 1000]


# read spectra ID
op2 = open(path_id, 'r')
lin2 = op2.readlines()
op2.close()

names_all = [elem.split() for elem in lin2[1:]]
names_max = [names_all[i][0] for i in xrange(len(names_all)) if names_all[i][-1] == '1']

groups = {}
for k in xrange(len(keys)):

    # read kmeans resulta
    op5 = open(path_set[k], 'r')
    lin5 = op5.readlines()
    op5.close()

    kmeans_classes = [float(elem.split()[0]) for elem in lin5]

    # separate groups according to kmeans classification
    groups_kmeans = []
    for item in xrange(ngroups):
        kmeans_temp = []
        cont = 0
        for j in xrange(len(names_all)):
            if names_all[j][-1] == '1':
                cont = cont + 1
                if kmeans_classes[cont - 1] == item:
                    kmeans_temp.append([names_all[j][0], names_all[j][3]])

        groups_kmeans.append(np.array(kmeans_temp))

    if len(groups_kmeans[0]) > len(groups_kmeans[1]):
        groups[keys[k]] = [groups_kmeans[1], groups_kmeans[0]]
    else:
        groups[keys[k]] = groups_kmeans


# identify the smaller group
pop_min = min([len(groups[key][0]) for key in keys])
pop_max = max([len(groups[key][1]) for key in keys])


# get the differences between sets
diff_sets = {}
for comp in keys:
    for other in keys:
        temp = []
        for ii in xrange(len(groups[comp][0])):
            if other != comp and groups[comp][0][ii][0] not in groups[other][0][:,0]:
                temp.append(groups[comp][0][ii])
        
        if other != comp and (other, comp) not in diff_sets.keys():     
            diff_sets[(comp, other)] = np.array(temp)


all_ids = []
names_diff = []
for k1 in diff_sets.keys():
    for k2 in diff_sets[k1]:
        if list(k2) not in all_ids:
            all_ids.append(list(k2))

        if k2[0] not in names_diff:
            names_diff.append(k2[0])

print 'len(names_diff) = ' + str(len(names_diff))

# count the most frequent missmatched classifications
mismatched = {}
for name in all_ids:
    mismatched[tuple(name)] = sum([name in ll for ll in diff_sets.values()])


op = open('mismatch_seeds_5f_2g.dat', 'w')
op.write('snid \t epoch \t number of mismatch\n')
for key in mismatched:
    op.write(str(key[0]) + '\t' + str(key[1]) + '\t' + str(mismatched[key]) + '\n')
op.close()


    

