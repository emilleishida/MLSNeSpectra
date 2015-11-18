from numpy import loadtxt, savetxt
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim
data_dir='../../data_all_types/'
out_dir='./plots/'

labels = loadtxt(data_dir+'labels.dat')
## plot the results
colors_vec=[]
for i in labels:
    if i ==1:
        colors_vec.append('r')
    if i ==0:
        colors_vec.append('w')
X = loadtxt('output_coeff.dat')
indexes = [0,4]
figure()
scatter(X[:, indexes[0]], X[:, indexes[1]], c=colors_vec, marker='.',linewidth=.1)
xlabel('PC %d' % (indexes[0]+1))
ylabel('PC %d' % (indexes[1]+1))
axis('equal')
savefig(out_dir+'scatter_plot_%d_%d.png' % (indexes[0]+1,indexes[1]+1))



