
from numpy import loadtxt, genfromtxt, savetxt, var, random
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim, ylim, legend

data_to_plot = loadtxt('./residuals.dat').T
figure()
#plot(data_to_plot[0], data_to_plot[1],'xr', label='PCA at max')
plot(data_to_plot[0], data_to_plot[2],'Dr', label='PCA with TL')
#plot(data_to_plot[0], data_to_plot[3],'xk', label='DL at max')
plot(data_to_plot[0], data_to_plot[4],'Dk', label='DL with TL')
ylabel('fractional variance')
xlabel('features')
ylim(0,1)
legend()

savefig('./plots/transfer_learning.png')

data_to_plot = loadtxt('./residuals_all_matrix.dat').T
figure()
plot(data_to_plot[0], data_to_plot[1],'or', label='PCA with all epochs')
plot(data_to_plot[0], data_to_plot[2],'ok', label='DL with all epochs')
ylabel('fractional variance')
xlabel('features')
ylim(0,1)
legend()

savefig('./plots/PCA_vs_DL.png')

