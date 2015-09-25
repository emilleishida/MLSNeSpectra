from numpy import loadtxt, shape, mean, sort, savetxt
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim, fill_between

in_data_dir='../../data/'
out_data_dir='../../data/'

# crop the wavelength range of a strong telluric line
wavelength_range_sel = range(300)+range(330,355,1)
# maximum error treshold
mean_error_treshold = 0.0011

derivatives_orig = loadtxt(in_data_dir+'derivatives_orig.dat')
errors_orig = loadtxt(in_data_dir+'errors_orig.dat')

derivatives = derivatives_orig.T[wavelength_range_sel].T
errors = errors_orig.T[wavelength_range_sel].T

## this is to plot the distribution of errors and select the treshold
#figure();plot(sort((mean(errors,1))))

sel_sne = [i for i in range(shape(errors)[0]) if mean(errors[i]) < mean_error_treshold]
derivatives = derivatives[sel_sne]
errors = errors[sel_sne]

savetxt(out_data_dir+'derivatives.dat', derivatives, header='Derivatives of the Log10 of the fluxes. Rows: SNe, Columns: Wavelengths')
savetxt(out_data_dir+'errors.dat', errors, header='Errors on the derivatives. Rows: SNe, Columns: Wavelengths')
