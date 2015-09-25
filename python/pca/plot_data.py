from numpy import loadtxt, shape
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim, fill_between

data_dir='../../data/'
out_dir='./plots/'

derivatives = loadtxt(data_dir+'derivatives.dat')
errors = loadtxt(data_dir+'errors.dat')

figure(figsize=(8,32))
for i in range(shape(derivatives)[0]):
    fill_between(range(shape(derivatives)[1]), derivatives[i]+errors[i] +i/100., derivatives[i]-errors[i] +i/100. , alpha=.3)
    plot(range(shape(derivatives)[1]), derivatives[i] +i/100., 'k')

savefig(out_dir+'input_data.pdf')
