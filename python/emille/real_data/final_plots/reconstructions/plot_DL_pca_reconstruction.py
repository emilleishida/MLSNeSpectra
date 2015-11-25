from numpy import loadtxt, genfromtxt, shape, mean, sort, savetxt, size, array, copy
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim, fill_between, legend, text, show
from sklearn.decomposition.pca import PCA
import pylab as plt
import numpy as np

# define data directory
data_dir= '../../../../../data_all_types/'

# read data
der = loadtxt(data_dir+'derivatives.dat')
flux = loadtxt(data_dir+'fluxes_not_res.dat.gz')
labels = loadtxt(data_dir+'labels.dat')
spectra_data = genfromtxt(data_dir+'spectra_data.dat',dtype=None)

# make pca reduction
pca = PCA(n_components=4)
pca.fit(der)
X = pca.transform(der)
pred_PCA = (pca.inverse_transform(X))
pca = PCA(n_components=15)
pca.fit(der)
X = pca.transform(der)
pred_PCA_15PC = (pca.inverse_transform(X))

# load deep learning results
pred_DL = loadtxt('../../../../../R/out_DeepLearning/predictions_120,100,90,50,30,20,4,20,30,50,90,100,120_seed1_dl.dat' )

# define wavelength range
wavelenght_array = array(range(3200,9000,2))
wavelenght_array = wavelenght_array[range(370,1850,1)]
wavelenght_array_flux = copy(wavelenght_array)
wavelenght_array = wavelenght_array[::5]

wavelenght_array_int = wavelenght_array[:]-5.

# plot
n_plot1 = 0

range_to_plot =[
 17,
 47,
 175,
 3174,
 1646,
 1794,
 2240,
26,
 108, 1401]
range_to_plot.reverse()


n_plot = size(range_to_plot)

axs = [[] for i in xrange(2)]
names = ['log10 flux', 'reconst. 4PCs', 'reconst. 15PCs', 'reconst. DL \n 4 features']

fig = plt.figure()
plt.subplot(1,2,1)
plt.plot(wavelenght_array_flux, flux[17], color='black', ls='--', lw=2.0)
plt.plot(wavelenght_array_flux, flux[175] + 1.5, color='black', ls='--', lw=2.0)
plt.plot(wavelenght_array_flux, flux[1794] + 3.0, color='black', ls='--', lw=2.0)
plt.plot(wavelenght_array_flux, flux[26] + 4.5, color='black', ls='--', lw=2.0)
plt.plot(wavelenght_array_flux, flux[108] + 6.0, color='black', ls='--', lw=2.0)
plt.plot(wavelenght_array_flux, flux[1401] + 7.5, color='black', ls='--', lw=2.0)

plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[17][:i]) for i in range(size(der[0]))]) + flux[17][0], color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[175][:i]) for i in range(size(der[0]))]) + flux[175][0] + 1.5, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[1794][:i]) for i in range(size(der[0]))]) + flux[1794][0] + 3.0, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[26][:i]) for i in range(size(der[0]))]) + flux[26][0] + 4.5, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[108][:i]) for i in range(size(der[0]))]) + flux[108][0] + 6.0, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[1401][:i]) for i in range(size(der[0]))]) + flux[1401][0] + 7.5, color='red', ls=':', lw=2.0)

plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[17][:i]) for i in range(size(der[0]))]) + flux[17][0], color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[175][:i]) for i in range(size(der[0]))]) + flux[175][0] + 1.5, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[1794][:i]) for i in range(size(der[0]))]) + flux[1794][0] + 3.0, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[26][:i]) for i in range(size(der[0]))]) + flux[26][0] + 4.5, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[108][:i]) for i in range(size(der[0]))]) + flux[108][0] + 6.0, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[1401][:i]) for i in range(size(der[0]))]) + flux[1401][0] + 7.5, color='green', ls='-.', lw=2.0)

plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[17][:i]) for i in range(size(der[0]))]) + flux[17][0], color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[175][:i]) for i in range(size(der[0]))]) + flux[175][0] + 1.5, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[1794][:i]) for i in range(size(der[0]))]) + flux[1794][0] + 3.0, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[26][:i]) for i in range(size(der[0]))]) + flux[26][0] + 4.5, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[108][:i]) for i in range(size(der[0]))]) + flux[108][0] + 6.0, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[1401][:i]) for i in range(size(der[0]))]) + flux[1401][0] + 7.5, color='blue', lw=1.5)

plt.text(3600, 1.15, 'SN%s \n %.1fd %d' % (spectra_data['f0'][17][2:],spectra_data['f3'][17], 17))
plt.text(3600, 1.15 + 1.5, 'SN%s \n %.1fd %d' % (spectra_data['f0'][175][2:],spectra_data['f3'][175], 175))
plt.text(3600, 1.15 + 2.75, 'SN%s \n %.1fd %d' % (spectra_data['f0'][1794][2:],spectra_data['f3'][1794], 1794))
plt.text(3600, 1.15 + 4.0, 'SN%s \n %.1fd %d' % (spectra_data['f0'][26][2:],spectra_data['f3'][26], 26))
plt.text(3600, 1.15 + 5.5, 'SN%s \n %.1fd %d' % (spectra_data['f0'][108][2:],spectra_data['f3'][108], 108))
plt.text(3600, 1.15 + 7.0, 'SN%s \n %.1fd %d' % (spectra_data['f0'][1401][2:],spectra_data['f3'][1401], 1401))

plt.xlabel('wavelength ($\AA$)', fontsize=18)
plt.ylabel('flux (arbitrary units)', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

axs = plt.subplot(1,2,2)
line,  = axs.plot(wavelenght_array_flux, flux[47], color='black', ls='--', label=names[0], lw=2.0)
plt.plot(wavelenght_array_flux, flux[3174] + 1.0, color='black', ls='--', lw=2.0)
plt.plot(wavelenght_array_flux, flux[1646] + 2.0, color='black', ls='--', lw=2.0)
plt.plot(wavelenght_array_flux, flux[2240] + 3.0, color='black', ls='--', lw=2.0)

line,  = axs.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[47][:i]) for i in range(size(der[0]))]) + flux[47][0], color='red', ls=':', lw=2.0, label=names[1])
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[3174][:i]) for i in range(size(der[0]))]) + flux[3174][0] + 1.0, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[1646][:i]) for i in range(size(der[0]))]) + flux[1646][0] + 2.0, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[2240][:i]) for i in range(size(der[0]))]) + flux[2240][0] + 3.0, color='red', ls=':', lw=2.0)

line,  = axs.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[47][:i]) for i in range(size(der[0]))]) + flux[47][0], color='green', ls='-.', lw=2.0, label=names[2])
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[3174][:i]) for i in range(size(der[0]))]) + flux[3174][0] + 1.0, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[1646][:i]) for i in range(size(der[0]))]) + flux[1646][0] + 2.0, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[2240][:i]) for i in range(size(der[0]))]) + flux[2240][0] + 3.0, color='green', ls='-.', lw=2.0)

line,  = axs.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[47][:i]) for i in range(size(der[0]))]) + flux[47][0], color='blue', lw=1.5, label=names[3])
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[3174][:i]) for i in range(size(der[0]))]) + flux[3174][0] + 1.0, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[1646][:i]) for i in range(size(der[0]))]) + flux[1646][0] + 2.0, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[2240][:i]) for i in range(size(der[0]))]) + flux[2240][0] + 3.0, color='blue', lw=1.5)

plt.text(3600, 1.15, 'SN%s \n %.1fd %d' % (spectra_data['f0'][47][2:],spectra_data['f3'][47], 47))
plt.text(3600, 1.15 + 1.0, 'SN%s \n %.1fd %d' % (spectra_data['f0'][3174][2:],spectra_data['f3'][3174], 3174))
plt.text(3600, 1.15 + 2.0, 'SN%s \n %.1fd %d' % (spectra_data['f0'][1646][2:],spectra_data['f3'][1646], 1646))
plt.text(3600, 1.15 + 3.0, 'SN%s \n %.1fd %d' % (spectra_data['f0'][2240][2:],spectra_data['f3'][2240], 2240))

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('wavelength ($\AA$)', fontsize=18)
plt.ylabel('flux (arbitrary units)', fontsize=18)
plt.ylim(0,4.6)

axs.legend(bbox_to_anchor=(1.015, 1.014), ncol=1, fancybox=True, fontsize=14)
plt.show()

