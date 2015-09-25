from numpy import loadtxt, shape
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim, fill_between

derivatives = loadtxt('../data/derivatives.dat')
errors = loadtxt('../data/errors.dat')

figure(figsize=(8,32))
for i in range(shape(derivatives)[0]):
    fill_between(range(shape(derivatives)[1]), derivatives[i]+errors[i] +i/100., derivatives[i]-errors[i] +i/100. , alpha=.3)
    plot(range(shape(derivatives)[1]), derivatives[i] +i/100., 'k')

savefig('./input_data.pdf')
