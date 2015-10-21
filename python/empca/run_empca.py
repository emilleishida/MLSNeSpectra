import os
import tarfile
from numpy import loadtxt, mean,ones
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim
from empca import empca
import sys

data_dir='../../data/'
out_dir='./plots/'

url_tar = "https://www.dropbox.com/s/q22paf70tyulvka/derivatives.dat.tgz?dl=0"
url_empca = "https://raw.githubusercontent.com/sbailey/empca/master/empca.py"


# load the data and run PCA

if "derivatives.dat" not in os.listdir("./"):
	
	os.system( "wget %s"%url_tar )
	
	os.system( "tar -xzf derivatives.dat.tgz*")
	os.system( "rm derivatives.dat.tgz?dl=0" )

if "empca.py" not in os.listdir("./"):
	
	os.system(  "wget %s"%url_empca )
	
	



derivatives = loadtxt('derivatives.dat')


errors = ones(derivatives.shape)



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
    savefig(out_dir+'scatter_plot_%d_%d.png' % (indexes[0]+1,indexes[1]+1))


