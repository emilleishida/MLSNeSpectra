from numpy import loadtxt, genfromtxt, shape, mean, sort, savetxt, size, array, copy
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim, fill_between, legend, text
from sklearn.decomposition.pca import PCA
data_dir= '../data_all_types/'
out_dir='./plots/'

der = loadtxt(data_dir+'derivatives.dat')
flux = loadtxt(data_dir+'fluxes_not_res.dat')
labels = loadtxt(data_dir+'labels.dat')
spectra_data = genfromtxt(data_dir+'spectra_data.dat',dtype=None)

pca = PCA(n_components=4)
pca.fit(der)
X = pca.transform(der)
pred_PCA = (pca.inverse_transform(X))
pca = PCA(n_components=15)
pca.fit(der)
X = pca.transform(der)
pred_PCA_15PC = (pca.inverse_transform(X))
pred_DL = loadtxt('out_DeepLearning/predictions_120,100,90,50,30,20,4,20,30,50,90,100,120_seed1_dl.dat' )


#range_to_plot=[1,2,3,4,5,6,10]
#range_to_plot=range(300)

#range_to_plot=[]
#labels_to_plot=[]
#for i in range(size(labels)):
#    if spectra_data['f3'][i]> 0.2 and spectra_data['f3'][i]<.5:
#        range_to_plot.append(i)
#        labels_to_plot.append('%s %.2f' % (spectra_data['f0'][i], spectra_data['f3'][i]))

figure(figsize=(8,16))
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

wavelenght_array = array(range(3200,9000,2))
wavelenght_array = wavelenght_array[range(370,1850,1)]
wavelenght_array_flux = copy(wavelenght_array)
wavelenght_array = wavelenght_array[::5]

wavelenght_array_int = wavelenght_array[:]-5.

#plot(wavelenght_array_int,-4*array([[sum(der[j][:i]) for i in range(size(der[0])) ] for j in range_to_plot]).T + range(shape(der)[0])[n_plot1:n_plot1+n_plot], 'k--')
plot(wavelenght_array_flux,  8*array([(flux[j])*.1-flux[j][0]*.1 for j in range_to_plot]).T + range(shape(der)[0])[n_plot1:n_plot1+n_plot], 'k')
#for k in range(size(range_to_plot)):
#    plot(wavelenght_array_flux,  8*array([(flux[j])*.1-flux[j][0]*.1 for j in range_to_plot]).T[k] + range(shape(der)[0])[n_plot1:n_plot1+n_plot], 'k',label=labels_to_plot[k])
plot(wavelenght_array_int,-4*array([[sum(pred_PCA[j][:i]) for i in range(size(der[0])) ] for j in range_to_plot]).T + range(shape(der)[0])[n_plot1:n_plot1+n_plot],'m')
plot(wavelenght_array_int,-4*array([[sum(pred_PCA_15PC[j][:i]) for i in range(size(der[0])) ] for j in range_to_plot]).T + range(shape(der)[0])[n_plot1:n_plot1+n_plot],'r')
plot(wavelenght_array_int,-4*array([[sum(pred_DL[j][:i]) for i in range(size(der[0])) ] for j in range_to_plot]).T + range(shape(der)[0])[n_plot1:n_plot1+n_plot],'y')

plot([],[],'k',label='log10 flux')
plot([],[],'m',label='reconstruction with 4PCs PCA')
plot([],[],'r',label='reconstruction with 15PCs PCA')
plot([],[],'y',label='reconstruction with DL 4features')
xlabel('Ang')
ylabel('Log10(flux)+const')
legend(loc=3)

ii=0
for i in range_to_plot:
    text(4000,ii, 'SN%s %.1fd %d' % (spectra_data['f0'][i][2:],spectra_data['f3'][i], i))
    ii+=1

savefig(out_dir+'reconstruction_examples.png')

