from numpy import loadtxt, mean, genfromtxt
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim
from sklearn import manifold

def load_colors(sne_list,type='Wang'):

    import urllib
    import numpy
    
    path1 = 'https://iopscience.iop.org/1538-3881/143/5/126/suppdata/aj427309t4_mrt.txt'
    op1 = urllib.urlopen(path1, 'r')
    
    lin1 = op1.readlines()
    op1.close()
    #data1 = [elem[17:].split() for elem in lin1[51:]]
    data1 = [elem[:16].split()[0] for elem in lin1[51:]]
    data2 = [elem[41:].split() for elem in lin1[51:]]
    
    for i in range(numpy.shape(data2)[0]):
        if numpy.size(data2[i])==1:
            data2[i]= [ data2[i][0],'nan']
    
    if type=='Wang':
        col_=[['HV','N','91bg','91T','nan'],['y','g','c','r','b']]
        index=1
    if type=='Branch':
        col_=[['BL','CN','CL','SS'],['y','g','r','b']]
        index=0
    color_list=[]
    for i in sne_list:
        if i[2:] in data1:
            color_list.append( col_[1][col_[0].index(data2[data1.index(i[2:])][index])])
        else:
            color_list.append('k')
    return color_list

################

#data_dir='../../data_all_epochs/' # this it to use all the epochs
data_dir='../../data/' # this it to use the spectra at max
out_dir='./plots/'

# load the data and run PCA
derivatives = loadtxt(data_dir+'derivatives.dat')
errors = loadtxt(data_dir+'errors.dat')
SNe_data = genfromtxt(data_dir+'SNe.txt',dtype=None)

if SNe_data[0][0]!='s':
    sne_list=[i[0] for i in SNe_data]
else:
    sne_list=SNe_data

centered_der = derivatives-mean(derivatives,0)

n_neighbors=15 # tested from 10 to 15
n_components=6 # tested from 4 to 8

X, err = manifold.locally_linear_embedding(centered_der, n_neighbors, n_components,
                                           reg=0.001, eigen_solver='auto', tol=1e-06,
                                           max_iter=100, method='modified',
                                           hessian_tol=0.0001, modified_tol=1e-12) # tested method "normal" and "modified"

################
## plot the results

for class_type in ['Wang','Branch']:
    color_list = load_colors(sne_list,type=class_type)

    for indexes in [[0,1],[0,2],[0,3],[0,4]]:
        figure()
        #scatter(X[:, indexes[0]], X[:, indexes[1]])
        scatter(X[:,indexes[0]], X[:,indexes[1]],c=color_list)
        xlabel('PC %d' % (indexes[0]+1))
        ylabel('PC %d' % (indexes[1]+1))
        axis('equal')
        savefig(out_dir+'scatter_plot_%d_%d_%s.png' % (indexes[0]+1,indexes[1]+1, class_type))
    
