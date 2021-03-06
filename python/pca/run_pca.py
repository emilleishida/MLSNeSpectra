from sklearn.decomposition.pca import PCA
from numpy import loadtxt, savetxt
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim

#data_dir='../../data/'
data_dir='../../data_all_types/'
out_dir='./plots/'

# load the data and run PCA
derivatives = loadtxt(data_dir+'derivatives.dat')
pca = PCA(n_components=10)
pca.fit(derivatives)
X = pca.transform(derivatives)

# plot the results
figure()
plot( range(1,pca.n_components+1), pca.explained_variance_ratio_, 'o')
xlim(0.5,pca.n_components+.5)
xlabel('PC_n')
ylabel('Variance (%)')
savefig(out_dir+'variance_plot.png')

#for indexes in [[0,1],[0,2],[0,3],[0,4]]:
#    figure()
#    scatter(X[:, indexes[0]], X[:, indexes[1]])
#    xlabel('PC %d' % (indexes[0]+1))
#    ylabel('PC %d' % (indexes[1]+1))
#    axis('equal')
#    savefig(out_dir+'scatter_plot_%d_%d.png' % (indexes[0]+1,indexes[1]+1))

savetxt('output_coeff.dat', X)

