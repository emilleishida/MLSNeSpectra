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

path1 = 'SNe.txt'
path2 = '../../real_data/pca_kmeans/red_data/reduced_data_pca_7PC_2groups.dat'
path3 = '../../../../data_all_types/spectra_data.dat'

n_neighbors = 10

################################################################################

# read SN names
op1 = open(path1, 'r')
lin1 = op1.readlines()
op1.close()

names = [elem.split()[0] for elem in lin1[:]]

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
op2 = open(path2, 'r')
lin2 = op2.readlines()
op2.close()

data2 = [elem.split() for elem in lin2]

pc_matrix = np.array([[float(item) for item in line] for line in data2])


# use isomap
Y = manifold.Isomap(n_neighbors, 2).fit_transform(pc_matrix)

# read name of SN in source file
op3 = open(path3, 'r')
lin3 = op3.readlines()
op3.close()

data3 = [elem.split() for elem in lin3[1:]]

# store projections in pc space
for k in xrange(len(data2)):
    if data3[k][0] in sn_info.keys() and data3[k][-1] == '0':
        sn_info[data3[k][0]]['proj'] = [float(item) for item in data2[k]]
        sn_info[data3[k][0]]['isomap'] = Y[k]

# separate projections in a single list for wang classification
wang_data_list = {}
wang_isomap = {}
for color in color_wang[2]['color']:
    wang_data_list[color] = []
    wang_isomap[color] = []
    for sn in sn_info.keys():
        if sn_info[sn]['color_wang'] == color and 'proj' in sn_info[sn].keys():
            wang_data_list[color].append(sn_info[sn]['proj'])       
            wang_isomap[color].append(sn_info[sn]['isomap'])
            

    wang_data_list[color] = np.array(wang_data_list[color])
    wang_isomap[color] = np.array(wang_isomap[color])

# separate projections in a single list for branch classification
branch_data_list = {}
branch_isomap = {}
for color in color_branch[2]['color']:
    branch_data_list[color] = []
    branch_isomap[color] = []
    for sn in sn_info.keys():
        if sn_info[sn]['color_branch'] == color and 'proj' in sn_info[sn].keys():
            branch_data_list[color].append(sn_info[sn]['proj'])
            branch_isomap[color].append(sn_info[sn]['isomap'])
           

    branch_data_list[color] = np.array(branch_data_list[color])
    branch_isomap[color] = np.array(branch_isomap[color])

# plot wang and branch classfications
plt.figure()
plt.subplot(1,2,1)
for i in xrange(len(color_wang[2]['color'])):
    plt.scatter(wang_data_list[color_wang[2]['color'][i]][:,0], wang_data_list[color_wang[2]['color'][i]][:,1], color=color_wang[2]['color'][i], marker=color_wang[2]['mark'][i], label=color_wang[2]['name'][i])

plt.legend(title='Wang classification')
plt.xlabel('PC1')
plt.ylabel('PC2')

plt.subplot(1,2,2)
for i in xrange(len(color_branch[2]['color'])):
    plt.scatter(branch_data_list[color_branch[2]['color'][i]][:,0], branch_data_list[color_branch[2]['color'][i]][:,1], color=color_branch[2]['color'][i], marker=color_branch[2]['mark'][i], label=color_branch[2]['name'][i])

plt.legend(title='Branch classification')
plt.xlabel('PC1')
plt.ylabel('PC2')

plt.show()

plt.figure()
plt.subplot(1,2,1)
for i in xrange(len(color_wang[2]['color'])):
    plt.scatter(wang_isomap[color_wang[2]['color'][i]][:,0], wang_isomap[color_wang[2]['color'][i]][:,1], color=color_wang[2]['color'][i], marker=color_wang[2]['mark'][i], label=color_wang[2]['name'][i])

plt.legend(title='Wang classification')
plt.xlabel('isomap 1')
plt.ylabel('isomap 2')

plt.subplot(1,2,2)
for i in xrange(len(color_branch[2]['color'])):
    plt.scatter(branch_isomap[color_branch[2]['color'][i]][:,0], branch_isomap[color_branch[2]['color'][i]][:,1], color=color_branch[2]['color'][i], marker=color_branch[2]['mark'][i], label=color_branch[2]['name'][i])

plt.legend(title='Branch classification')
plt.xlabel('isomap 1')
plt.ylabel('isomap 2')

plt.show()






