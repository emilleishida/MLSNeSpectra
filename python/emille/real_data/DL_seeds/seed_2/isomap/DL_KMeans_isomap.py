import pylab as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from sklearn import manifold

def load_colors(sne_list,type='Wang'):

    import urllib
    import numpy
    
    #path1 = 'https://iopscience.iop.org/1538-3881/143/5/126/suppdata/aj427309t4_mrt.txt'
    #op1 = urllib.urlopen(path1, 'r')
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


# path to DL results
path_small_space = '../out/out_120,100,90,50,30,20,5,20,30,50,90,100,120_seed2_dl.dat'

# path to spectra ID
path_id = '../../../../../../data_all_types/spectra_data.dat'

# path to kmeans result
path_kmeans = '../cl_data/clustering_KMeans_label_5PC_2groups.dat'

# color for plotting
c = [ 'green', 'red', 'blue', 'orange', 'black']

# markers for ploting
mark =  ['^','o',  's', 'd', '*']

# markers size
size = [75, 65, 65, 70, 75]

# read spectra ID
op2 = open(path_id, 'r')
lin2 = op2.readlines()
op2.close()

names_all = [elem.split() for elem in lin2[1:]]
names_max = [names_all[i][0] for i in xrange(len(names_all)) if names_all[i][-1] == '1']

# build wang color code 
color_wang = load_colors(names_max)

# separate groups accorging to wang classification
wang_code = []
for cor in color_wang[2]['color']:
    temp_code = np.array(color_wang[0]) == cor
    wang_code.append(temp_code)


# read DL results
op1 = open(path_small_space, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

matrix = np.array([[float(item) for item in data1[i]] for i in xrange(len(data1)) if names_all[i][-1]=='1'])


# do isomap reduction
n_neighbors = 10
n_components = 2
Y = manifold.Isomap(n_neighbors, n_components).fit_transform(matrix)

# read kmeans results
op3 = open(path_kmeans, 'r')
lin3 = op3.readlines()
op3.close()

classes = np.array([float(elem.split()[0]) for elem in lin3])
group1 = classes == 0.0
group2 = classes == 1.0

# plot isomap reduction results
panels = [[] for i in xrange(2)]
plt.figure(figsize=(20,14))
fig1 = plt.subplot(1,2,1)
panels[0] = plt.scatter(Y[group1, 0], Y[group1, 1], color=c[0], marker=mark[0], s=75)
panels[1] = plt.scatter(Y[group2, 0], Y[group2, 1], color=c[1], marker=mark[1], s=65)
legs=fig1.legend(panels, ['Group 1', 'Group 2', 'Group 3'], loc = (0.0, 0.889), title='Kmeans classfication', fontsize=22)
plt.setp(legs.get_title(),fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlim(-2.0, 2.5)
plt.ylim(-2.0, 2.5)
plt.xlabel('isomap 1', fontsize=22)
plt.ylabel('isomap 2', fontsize=22)

panels2 = [[] for i in xrange(5)]
names = []
fig2 = plt.subplot(1,2,2)
for j in [0,1,2,3,4]:
    panels2[j] = plt.scatter(Y[wang_code[j],0], Y[wang_code[j],1], marker=mark[j], color=c[j], s=size[j])
    if color_wang[2]['name'][j] != 'nan':
        names.append(color_wang[2]['name'][j])
    else:
        names.append('peculiar')
legs2=fig2.legend(panels2, names, loc = (0.0, 0.784), title='Wang classification', fontsize=22)
plt.setp(legs2.get_title(),fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.tight_layout()
plt.xlim(-2.0, 2.5)
plt.ylim(-2.0, 2.5)
plt.xlabel('isomap 1', fontsize=22)
plt.ylabel('isomap 2', fontsize=22)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.tight_layout()
plt.savefig("seed2_5f_2g_kmeans_wang_isomap.pdf", format='pdf',dpi=1000)

