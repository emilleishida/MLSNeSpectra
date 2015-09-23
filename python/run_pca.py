from sklearn.decomposition.pca import PCA
from numpy import loadtxt
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim

# load the data and run PCA
derivatives = loadtxt('../data/derivatives.dat')
pca = PCA(n_components=10)
pca.fit(derivatives.T)
X = pca.transform(derivatives.T)

# plot the results
figure()
plot( range(1,pca.n_components+1), pca.explained_variance_ratio_, 'o')
xlim(0.5,pca.n_components+.5)
xlabel('PC_n')
ylabel('Variance (%)')
savefig('./variance_plot.pdf')

for indexes in [[0,1],[0,2],[0,3],[0,4]]:
    figure()
    scatter(X[:, indexes[0]], X[:, indexes[1]])
    xlabel('PC %d' % (indexes[0]+1))
    ylabel('PC %d' % (indexes[1]+1))
    axis('equal')
    savefig('./scatter_plot_%d_%d.pdf' % (indexes[0]+1,indexes[1]+1))


