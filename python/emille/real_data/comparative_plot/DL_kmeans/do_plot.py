from numpy import loadtxt, mean, genfromtxt
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim
from sklearn import manifold
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
import pylab as plt
import numpy as np

def load_colors(sne_list,type='Wang'):

    import urllib
    import numpy
    
    path1 = 'https://iopscience.iop.org/1538-3881/143/5/126/suppdata/aj427309t4_mrt.txt'
    op1 = urllib.urlopen(path1, 'r')
    op1=open('aj427309t4_mrt.txt','r')
    lin1 = op1.readlines()
    op1.close()
    #data1 = [elem[17:].split() for elem in lin1[51:]]
    data1 = [elem[:16].split()[0] for elem in lin1[51:]]
    data2 = [elem[41:].split() for elem in lin1[51:]]
    
    for i in range(numpy.shape(data2)[0]):
        if numpy.size(data2[i])==1:
            data2[i]= [ data2[i][0],'nan']
    
    if type=='Wang':
        name_dict={'name':['HV','N','91bg','91T','nan'],
                   'color':['y','g','c','r','b'],
                   'mark':[u"s",u"o",u"2",u"D",u"*"]}

        index=1
    if type=='Branch':
        name_dict={'name':['BL','CN','CL','SS'],
                   'color':['y','g','r','b'],
                   'mark':[u"s",u"o",u"2",u"D"]}
        index=0

    col_=[name_dict['name'],name_dict['color']]
    mark_=[name_dict['name'],name_dict['mark']]
    color_list=[]
    shape_list=[]
    for i in sne_list:
        if i[2:] in data1:
            color_list.append( col_[1][col_[0].index(data2[data1.index(i[2:])][index])])
            shape_list.append(mark_[1][mark_[0].index(data2[data1.index(i[2:])][index])])
        else:
            color_list.append('k')
            shape_list.append(u'x')
    return color_list,shape_list,name_dict


################################################################################
### User choices

npcs = '4'
ngroups = '2'
n_neighbors = 10

path_names = '../../../../../data_all_types/spectra_data.dat'
path_pcspace = '../../../../../R/out_DeepLearning/out_120,100,90,50,30,20,' + npcs + ',20,30,50,90,100,120_seed1_dl.dat'
path_groups = '../../../real_data/DL_kmeans/cl_data/clustering_KMeans_label.dat'



################################################################################

# read SN names
op1 = open(path_names, 'r')
lin1 = op1.readlines()
op1.close()

names_all = [elem.split() for elem in lin1[:]]
names = [line[0] for line in names_all if line[-1] == '1']

# build color code 
color_wang = load_colors(names)

# build dictionary
sn_info = {}
for i in xrange(len(names)):
    sn_info[names[i]] = {}
    sn_info[names[i]]['color_wang'] = color_wang[0][i]
    sn_info[names[i]]['marker_wang'] = color_wang[1][i]

    for j in xrange(len(color_wang[2]['name'])):
        if sn_info[names[i]]['color_wang'] == color_wang[2]['color'][j]:
            sn_info[names[i]]['type_wang'] = color_wang[2]['name'][j] 
            break

# build branch color code
color_branch = load_colors(names, type='Branch')

# fill dictionary
for i in xrange(len(names)):
    sn_info[names[i]]['color_branch'] = color_branch[0][i]
    sn_info[names[i]]['marker_branch'] = color_branch[1][i]

    for j in xrange(len(color_branch[2]['name'])):
        if sn_info[names[i]]['color_branch'] == color_branch[2]['color'][j]:
            sn_info[names[i]]['type_branch'] = color_branch[2]['name'][j] 
            break


# read PC space
op2 = open(path_pcspace, 'r')
lin2 = op2.readlines()
op2.close()

data2 = [elem.split() for elem in lin2]

pc_matrix = np.array([[float(item) for item in line] for line in data2])
pc_matrix_small = np.array([pc_matrix[i] for i in xrange(len(pc_matrix)) if names_all[i][-1] == '1'])


# use isomap
Y2 = manifold.Isomap(n_neighbors, 2).fit_transform(pc_matrix)
Y3 = manifold.Isomap(n_neighbors, 3).fit_transform(pc_matrix)

# store projections in pc space
for k in xrange(len(data2)):
    if names_all[k][0] in sn_info.keys() and names_all[k][-1] == '0':
        if 'proj' not in sn_info[names_all[k][0]].keys():
            sn_info[names_all[k][0]]['proj'] = [[float(item) for item in data2[k]]]
            sn_info[names_all[k][0]]['isomap2'] = [Y2[k]]
            sn_info[names_all[k][0]]['isomap3'] = [Y3[k]]
        else:
            sn_info[names_all[k][0]]['proj'].append([float(item) for item in data2[k]])
            sn_info[names_all[k][0]]['isomap2'].append(Y2[k])
            sn_info[names_all[k][0]]['isomap3'].append(Y3[k])

# separate projections in a single list for wang classification
wang_data_list = {}
wang_isomap2 = {}
wang_isomap3 = {}
for color in color_wang[2]['color']:
    wang_data_list[color] = []
    wang_isomap2[color] = []
    wang_isomap3[color] = []
    for sn in sn_info.keys():
        if sn_info[sn]['color_wang'] == color and 'proj' in sn_info[sn].keys():
            for l in xrange(len(sn_info[sn]['proj'])):
                wang_data_list[color].append(sn_info[sn]['proj'][l])       
                wang_isomap2[color].append(sn_info[sn]['isomap2'][l])
                wang_isomap3[color].append(sn_info[sn]['isomap3'][l])

    wang_data_list[color] = np.array(wang_data_list[color])
    wang_isomap2[color] = np.array(wang_isomap2[color])
    wang_isomap3[color] = np.array(wang_isomap3[color])

# separate projections in a single list for branch classification
branch_data_list = {}
branch_isomap2 = {}
branch_isomap3 = {}
for color in color_branch[2]['color']:
    branch_data_list[color] = []
    branch_isomap2[color] = []
    branch_isomap3[color] = []
    for sn in sn_info.keys():
        if sn_info[sn]['color_branch'] == color and 'proj' in sn_info[sn].keys():
            for l in xrange(len(sn_info[sn]['proj'])):
                branch_data_list[color].append(sn_info[sn]['proj'][l])
                branch_isomap2[color].append(sn_info[sn]['isomap2'][l])
                branch_isomap3[color].append(sn_info[sn]['isomap3'][l])
           

    branch_data_list[color] = np.array(branch_data_list[color])
    branch_isomap2[color] = np.array(branch_isomap2[color])
    branch_isomap3[color] = np.array(branch_isomap3[color])

# read groups find by clustering
op4 = open(path_groups, 'r')
lin4 = op4.readlines()
op4.close()

clustering = [float(elem.split()[0]) for elem in lin4]

# plot wang and branch classfications
pc0 = 2
pc1 = 3
plt.figure()
plt.subplot(1,2,1)
for i in xrange(len(color_wang[2]['color'])):
    plt.scatter(wang_data_list[color_wang[2]['color'][i]][:,pc0], wang_data_list[color_wang[2]['color'][i]][:,pc1], color=color_wang[2]['color'][i], marker=color_wang[2]['mark'][i], label=color_wang[2]['name'][i])

plt.legend(title='Wang classification')
plt.xlabel('PC' + str(pc0 + 1))
plt.ylabel('PC' + str(pc1 + 1))
plt.xlim(-1.5,1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(1,2,2)
for i in xrange(len(color_branch[2]['color'])):
    plt.scatter(branch_data_list[color_branch[2]['color'][i]][:,pc0], branch_data_list[color_branch[2]['color'][i]][:,pc1], color=color_branch[2]['color'][i], marker=color_branch[2]['mark'][i], label=color_branch[2]['name'][i])

plt.legend(title='Branch classification')
plt.xlabel('PC' + str(pc0 + 1))
plt.ylabel('PC' + str(pc1 + 1))
plt.xlim(-1.5,1.5)
plt.ylim(-1.5, 1.5)


plt.show()

plt.figure()
plt.subplot(1,2,1)
for i in xrange(len(color_wang[2]['color'])):
    plt.scatter(wang_isomap2[color_wang[2]['color'][i]][:,0], wang_isomap2[color_wang[2]['color'][i]][:,1], color=color_wang[2]['color'][i], marker=color_wang[2]['mark'][i], label=color_wang[2]['name'][i])

plt.legend(title='Wang classification')
plt.xlabel('isomap 1')
plt.ylabel('isomap 2')

plt.subplot(1,2,2)
for i in xrange(len(color_branch[2]['color'])):
    plt.scatter(branch_isomap2[color_branch[2]['color'][i]][:,0], branch_isomap2[color_branch[2]['color'][i]][:,1], color=color_branch[2]['color'][i], marker=color_branch[2]['mark'][i], label=color_branch[2]['name'][i])

plt.legend(title='Branch classification')
plt.xlabel('isomap 1')
plt.ylabel('isomap 2')

plt.show()


plt.figure()
plt.subplot(1,3,1)
for i in xrange(len(color_wang[2]['color'])):
    plt.scatter(wang_isomap2[color_wang[2]['color'][i]][:,0], wang_isomap2[color_wang[2]['color'][i]][:,1], color=color_wang[2]['color'][i], marker=color_wang[2]['mark'][i], label=color_wang[2]['name'][i])

plt.legend(title='Wang classification')
plt.xlabel('isomap 1')
plt.ylabel('isomap 2')

plt.subplot(1,3,1)
for i in xrange(len(color_wang[2]['color'])):
    print color_wang[2]['color'][i]
    plt.scatter(wang_isomap3[color_wang[2]['color'][i]][:,0], wang_isomap3[color_wang[2]['color'][i]][:,1], color=color_wang[2]['color'][i], marker=color_wang[2]['mark'][i], label=color_wang[2]['name'][i])

plt.legend(title='isomap')
plt.xlabel('isomap 1')
plt.ylabel('isomap 2')

for i in xrange(len(color_wang[2]['color'])):
    plt.scatter(wang_isomap3[color_wang[2]['color'][i]][:,0], wang_isomap3[color_wang[2]['color'][i]][:,2], color=color_wang[2]['color'][i], marker=color_wang[2]['mark'][i], label=color_wang[2]['name'][i])

plt.legend(title='isomap')
plt.xlabel('isomap 1')
plt.ylabel('isomap 3')

for i in xrange(len(color_wang[2]['color'])):
    plt.scatter(wang_isomap3[color_wang[2]['color'][i]][:,1], wang_isomap3[color_wang[2]['color'][i]][:,2], color=color_wang[2]['color'][i], marker=color_wang[2]['mark'][i], label=color_wang[2]['name'][i])

plt.legend(title='isomap')
plt.xlabel('isomap 2')
plt.ylabel('isomap 3')
plt.show()






