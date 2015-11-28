import pylab as plt
import numpy as np

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
path_small_space = '../../../../../R/out_DeepLearning/out_120,100,90,50,30,20,4,20,30,50,90,100,120_seed1_dl.dat'

# path to spectra ID
path_id = '../../../../../data_all_types/spectra_data.dat'

# path to original spectra
path_spectra = '../../../../../data_all_types/fluxes.dat'

# path to kmeans result 4 groups
path_kmeans_4g = '../../DL_kmeans/cl_data_all/clustering_KMeans_label_4PC_4groups.dat'

# read kmeans result 4 groups
op5 = open(path_kmeans_4g, 'r')
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

# build branch color code 
color_branch = load_colors(names_max, type='Branch')

# separate groups accorging to branch classification
branch_spectra = []
for cor in color_branch[2]['color']:
    spectra_temp = []
    cont = 0
    for j in xrange(len(data_spectra)):
        if names_all[j][-1] == '1':
            cont = cont + 1
            if color_branch[0][cont - 1] == cor:
                spectra_temp.append(data_spectra[j])
            
    spectra_temp = np.array(spectra_temp)
    branch_spectra.append(spectra_temp)

branch_spectra = np.array(branch_spectra)

spectra_group = []
for j in xrange(len(branch_spectra)):
    spectra_group.append([np.mean(branch_spectra[j][:,l]) for l in xrange(len(branch_spectra[j][0]))])

spectra_group = np.array(spectra_group)


# separate groups according to kmeans classification 4 groups
groups_kmeans = []
for item in xrange(4):
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
xaxes = [4000 + 10*ll for ll in xrange(len(data_spectra[0]))]

# plot branch and kmeans results
fig2 = plt.figure(figsize=(18,12))
ax = plt.subplot(111)
line, = ax.plot(xaxes, spectra_group[color_branch[2]['name'].index('BL')]+1.6, lw=4.0, ls='--', color='green', label='BL - Branch')
line,  = ax.plot(xaxes, spectra_group[color_branch[2]['name'].index('CN')]+1.1, lw=4.0,ls='--', color='red', label='CN - Branch')
line, = ax.plot(xaxes, spectra_group[color_branch[2]['name'].index('CL')]+0.6, lw=4.0, ls='--', color='blue', label='CL - Branch')
line, = ax.plot(xaxes, spectra_group[color_branch[2]['name'].index('SS')], lw=4.0, ls='--', color='orange', label='SS - Branch')
line, = ax.plot(xaxes, kmeans_rep[0]+1.6, color='green',lw=4.0, label='DL+KM G1')
line, = ax.plot(xaxes, kmeans_rep[1]+1.1, lw=4.0, color='red', label='DL+KM G2')
line, = ax.plot(xaxes, kmeans_rep[2]+0.6, lw=4.0, color='blue', label='DL+KM G3')
line, = ax.plot(xaxes, kmeans_rep[3], lw=4.0, color='orange', label='DL+KM G4')
plt.xlabel('wavelength ($\AA$)', fontsize=26)
plt.ylabel('flux (arbitrary units)', fontsize=26)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.tight_layout()
plt.ylim(0, 2.6)
ax.legend(loc='upper center', bbox_to_anchor=(0.831, 1.013), ncol=2, fontsize=20)
plt.savefig("branch_DL_kmeans_spectra_4g.pdf", format='pdf',dpi=1000)


