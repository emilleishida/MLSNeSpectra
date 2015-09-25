from numpy import loadtxt, mean
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim
from empca import empca

# load the data and run PCA
derivatives = loadtxt('../data/derivatives.dat')
errors = loadtxt('../data/errors.dat')

centered_der = derivatives-mean(derivatives,0)

m = empca(centered_der, 1./(errors)**2, nvec=5,smooth=0, niter=50)

X = m.coeff

## plot the results

for indexes in [[0,1],[0,2],[0,3],[0,4]]:
    figure()
    scatter(X[:, indexes[0]], X[:, indexes[1]])
    xlabel('PC %d' % (indexes[0]+1))
    ylabel('PC %d' % (indexes[1]+1))
    axis('equal')
    savefig('./scatter_plot_%d_%d.pdf' % (indexes[0]+1,indexes[1]+1))


