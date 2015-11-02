import pylab as plt
import numpy as np

path1 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/R/out_DeepLearning/out_120,100,90,50,30,20,2,20,30,50,90,100,120_dl.dat'
path2 = '/home/emille/Documents/github/mlsnespectra/MLSNeSpectra/data_all_types/labels.dat'

op1 = open(path1, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

data = np.array([[float(elem) for elem in line] for line in data1])

plt.figure()
plt.scatter(data[:,0], data[:,1])
plt.show()

op2 = open(path2, 'r')
lin2 = op2.readlines()
op2.close()

data2 = [elem.split()[0] for elem in lin2]

data_plot = np.array([data1[i] for i in xrange(len(data1)) if data2[i] == '1'])

plt.figure()
plt.scatter(data_plot[:,0], data_plot[:,1])
plt.show()

"""
op3 = open('../red_data/reduce_data_DL.dat', 'w')
for line in data_plot:
    for elem in line:
        op3.write(str(elem) + '    ')
    op3.write('\n')
op3.close()
"""

op4 = open('../red_data/reduced_data_KMeans_label.dat', 'r')
lin4 = op4.readlines()
op4.close()

data4 = [float(elem.split()[0]) for elem in lin4]

data_g1 = np.array([data_plot[i] for i in xrange(len(data_plot)) if data4[i] == 1.0])
data_g2 = np.array([data_plot[i] for i in xrange(len(data_plot)) if data4[i] == 0.0])
if 2.0 in data4:
    data_g3 = np.array([data_plot[i] for i in xrange(len(data_plot)) if data4[i] == 2.0])
if 3.0 in data4:
    data_g4 = np.array([data_plot[i] for i in xrange(len(data_plot)) if data4[i] == 3.0])
if 4.0 in data4:
    data_g5 = np.array([data_plot[i] for i in xrange(len(data_plot)) if data4[i] == 4.0])


plt.figure()
plt.scatter(data_g1[:,0], data_g1[:,1], color='red')
plt.scatter(data_g2[:,0], data_g2[:,1], color='blue')
if 2.0 in data4:
    plt.scatter(data_g3[:,0], data_g3[:,1], color='green')
if 3.0 in data4:
    plt.scatter(data_g4[:,0], data_g4[:,1], color='brown')
if 4.0 in data4:
    plt.scatter(data_g5[:,0], data_g5[:,1], color='purple')

plt.show()

