from numpy import loadtxt, mean, genfromtxt
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim
from sklearn import manifold
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
import pylab as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

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
###############################################################################################


# number of features in DL results
nfeatures = '4'

# path to DL results
path_small_space = '../../../../../R/out_DeepLearning/out_120,100,90,50,30,20,' + nfeatures + ',20,30,50,90,100,120_seed1_dl.dat'

# path to spectra ID
path_id = '../../../../../data_all_types/spectra_data.dat'

# path to original spectra
path_spectra = '../../../../../data_all_types/fluxes.dat'


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

# build wang color code 
color_wang = load_colors(names_max)
color_wang[2]['mark'] = ['^','o',  's', 'd', '*']



wang_code = []
wang_spectra = []
for cor in color_wang[2]['color'][:-1]:
    temp_code = np.array(color_wang[0]) == cor
    wang_code.append(temp_code)

    spectra_temp = []
    for j in xrange(len(color_wang[0])):
        if color_wang[0][j] == cor:
            spectra_temp.append(data_spectra[j])
    spectra_temp = np.array(spectra_temp)

    wang_spectra.append(spectra_temp)

wang_spectra = np.array(wang_spectra)

spectra_group = []
for j in xrange(len(wang_spectra)):
    spectra_group.append([np.mean(wang_spectra[j][:,l]) for l in xrange(len(wang_spectra[j][0]))])

# plot mean spectra from wang
plt.figure()
for l in [3,0,2,1]:
    plt.plot([4000 + 10*x for x in xrange(len(spectra_group[0]))], spectra_group[l], lw=1.5, color=color_wang[2]['color'][l], label=color_wang[2]['name'][l])
leg = plt.legend(title='Wang classification', fontsize=18)
plt.setp(leg.get_title(),fontsize=18)
plt.xlabel('wavelength', fontsize=22)
plt.ylabel('flux (arbtrary units)', fontsize=22)
plt.show()


color_wang[2]['color'] = ['red', 'green', 'blue', 'orange']

# build branch color code 
color_branch = load_colors(names_max, type='Branch')
branch_code = []
for cor in color_branch[2]['color']:
    temp_code = np.array(color_branch[0]) == cor
    branch_code.append(temp_code)


# read DL results
op1 = open(path_small_space, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

matrix = np.array([[float(item) for item in data1[i]] for i in xrange(len(data1)) if names_all[i][-1]=='1'])


# plot only DL results
fig = plt.figure()
plt.subplot(4,4,1)
legs = [[] for k in xrange(len(wang_code))]
for j in xrange(len(wang_code)):
    legs[j] = plt.scatter(matrix[wang_code[j],0], matrix[wang_code[j],0], lw='0',marker=color_wang[2]['mark'][j],s=14, color=color_wang[2]['color'][j])
plt.ylabel('feature 1', fontsize=18)
plt.xticks([])
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,5)
for j in xrange(len(wang_code)):
    plt.scatter(matrix[wang_code[j],0], matrix[wang_code[j],1], lw='0',marker=color_wang[2]['mark'][j],s=14, color=color_wang[2]['color'][j])
plt.ylabel('feature 2', fontsize=18)
plt.xticks([])
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,6)
for j in xrange(len(wang_code)):
    plt.scatter(matrix[wang_code[j],1], matrix[wang_code[j],1], lw='0',marker=color_wang[2]['mark'][j],s=14, color=color_wang[2]['color'][j])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,9)
for j in xrange(len(wang_code)):
    plt.scatter(matrix[wang_code[j],0], matrix[wang_code[j],2], lw='0',marker=color_wang[2]['mark'][j],s=14, color=color_wang[2]['color'][j])
plt.ylabel('feature 3', fontsize=18)
plt.xticks([])
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,10)
for j in xrange(len(wang_code)):
    plt.scatter(matrix[wang_code[j],1], matrix[wang_code[j],2], lw='0',marker=color_wang[2]['mark'][j],s=14, color=color_wang[2]['color'][j])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,11)
for j in xrange(len(wang_code)):
    plt.scatter(matrix[wang_code[j],2], matrix[wang_code[j],2], lw='0',marker=color_wang[2]['mark'][j],s=14, color=color_wang[2]['color'][j])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,13)
for j in xrange(len(wang_code)):
    plt.scatter(matrix[wang_code[j],0], matrix[wang_code[j],3], lw='0',marker=color_wang[2]['mark'][j],s=14, color=color_wang[2]['color'][j])
plt.ylabel('feature 4', fontsize=18)
plt.xlabel('feature 1', fontsize=18)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,14)
for j in xrange(len(wang_code)):
    plt.scatter(matrix[wang_code[j],1], matrix[wang_code[j],3], lw='0',marker=color_wang[2]['mark'][j],s=14, color=color_wang[2]['color'][j])
plt.xlabel('feature 2', fontsize=18)
plt.yticks([])
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,15)
for j in xrange(len(wang_code)):
    plt.scatter(matrix[wang_code[j],2], matrix[wang_code[j],3], lw='0',marker=color_wang[2]['mark'][j],s=14, color=color_wang[2]['color'][j])
plt.xlabel('feature 3',fontsize=18)
plt.yticks([])
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,16)
for j in xrange(len(wang_code)):
    plt.scatter(matrix[wang_code[j],3], matrix[wang_code[j],3], lw='0',marker=color_wang[2]['mark'][j],s=14, color=color_wang[2]['color'][j])
plt.xlabel('feature 4', fontsize=18)
plt.yticks([])
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15,hspace=0.0,wspace=0.0)
fig.legend([legs[3], legs[0], legs[2], legs[1]], [color_wang[2]['name'][3],color_wang[2]['name'][0], color_wang[2]['name'][2], color_wang[2]['name'][1]], loc = (0.807, 0.735), title='Wang classification', fontsize=18)
plt.show()

