import pylab as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

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

# read spectra ID
op2 = open(path_id, 'r')
lin2 = op2.readlines()
op2.close()

names_all = [elem.split() for elem in lin2[1:]]
names_max = [names_all[i][0] for i in xrange(len(names_all)) if names_all[i][-1] == '1']


# build branch color code 
color_branch = load_colors(names_max, type='Branch')

# separate groups accorging to branch classification
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

my_colors = ['green', 'red', 'blue', 'orange']
my_marks = ['^','o',  's', 'd', '*']

# marker size
ss = [60, 40, 40, 60]

# plot only DL results
fig = plt.figure(figsize=(20,14))
plt.subplot(4,4,1)
legs = [[] for k in xrange(len(branch_code))]
names = []
for j in [0,1,2,3]:
    legs[j] = plt.scatter(matrix[branch_code[j],0], matrix[branch_code[j],0], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
    names.append(color_branch[2]['name'][j])
plt.ylabel('feature 1', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,5)
for j in xrange(len(branch_code)):
    plt.scatter(matrix[branch_code[j],0], matrix[branch_code[j],1], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.ylabel('feature 2', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,6)
for j in xrange(len(branch_code)):
    plt.scatter(matrix[branch_code[j],1], matrix[branch_code[j],1], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,9)
for j in xrange(len(branch_code)):
    plt.scatter(matrix[branch_code[j],0], matrix[branch_code[j],2], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.ylabel('feature 3', fontsize=26)
plt.xticks([])
plt.yticks(fontsize=22)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,10)
for j in xrange(len(branch_code)):
    plt.scatter(matrix[branch_code[j],1], matrix[branch_code[j],2], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,11)
for j in xrange(len(branch_code)):
    plt.scatter(matrix[branch_code[j],2], matrix[branch_code[j],2], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xticks([])
plt.yticks([])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,13)
for j in xrange(len(branch_code)):
    plt.scatter(matrix[branch_code[j],0], matrix[branch_code[j],3], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.ylabel('feature 4', fontsize=26)
plt.xlabel('feature 1', fontsize=26)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,14)
for j in xrange(len(branch_code)):
    plt.scatter(matrix[branch_code[j],1], matrix[branch_code[j],3], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xlabel('feature 2', fontsize=26)
plt.yticks([])
plt.xticks(fontsize=22)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,15)
for j in xrange(len(branch_code)):
    plt.scatter(matrix[branch_code[j],2], matrix[branch_code[j],3], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xlabel('feature 3',fontsize=26)
plt.yticks([])
plt.xticks(fontsize=22)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(4,4,16)
for j in xrange(len(branch_code)):
    plt.scatter(matrix[branch_code[j],3], matrix[branch_code[j],3], lw='0',marker=my_marks[j],s=ss[j], color=my_colors[j])
plt.xlabel('feature 4', fontsize=26)
plt.yticks([])
plt.xticks(fontsize=22)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6, prune='upper'))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)



plt.subplots_adjust(left=0.075, right=0.975, top=0.975, bottom=0.075,hspace=0.0,wspace=0.0)
legend = fig.legend(legs, names, loc = (0.786, 0.778), title='Branch classification', fontsize=26)
plt.setp(legend.get_title(),fontsize=26)
plt.savefig("branch_DL_scatter.pdf", format='pdf',dpi=1000)


