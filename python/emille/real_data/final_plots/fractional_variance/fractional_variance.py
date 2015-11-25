import pylab as plt
import numpy as np
from numpy import loadtxt

# path to DL and DL no transfer learning data
path_var1 = '../../../../transfer_learning_test/residuals.dat'

# read data
op1 = open(path_var1, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1[1:]]

data_to_plot = np.array([[float(item) for item in line] for line in data1])

# plot DL results with and without TL
plt.figure()
plt.scatter(data_to_plot[:,0], data_to_plot[:,3], color='black', marker = 'o', label='DL only at max')
plt.scatter(data_to_plot[:,0], data_to_plot[:,4], color='red', marker='^', label='DL at all epochs')
plt.show()
