import sn_simulator
import pylab as plt
import numpy as np

##############################################################################
### User input

# number of fake data for each one of the 3 extreme values
ndata = 100

# fraction of total variance around the original projection
sim_std = 0.8

# PCs to be plotted
PCx = 0
PCy = 1

# simulated epoch
epoch = 0.0

# generate plot 1-> yes, 0-> no
plot = 1

##############################################################################


# read tranining set projections
train_data = sn_simulator.load_training_coeff()


# identify SN with highest PC1 coefficient
indx_xmax = list(train_data[1][:,PCx]).index(max(train_data[1][:,PCx]))

# identify SN with lowest PC1 coefficient
indx_xmin = list(train_data[1][:,PCx]).index(min(train_data[1][:,PCx]))

# identify SN with lowest PC2 coefficient
indx_ymin = list(train_data[1][:,PCy]).index(min(train_data[1][:,PCy]))


# calculate scatter in all directions
std = []
for j in xrange(len(train_data[1][0])):
    std.append(np.std(train_data[1][:,j]))

# generate fake data around the extreme values 
new_data = []
new_proj = []
for i in xrange(ndata):
    xmax_proj = [np.random.normal(loc=train_data[1][indx_xmax][j], scale=sim_std * std[j])
                 for j in xrange(len(train_data[1][0]))]

    new_proj.append(xmax_proj)

    new_data.append(sn_simulator.simulated_der(xmax_proj, epoch))

    xmin_proj = [np.random.normal(loc=train_data[1][indx_xmin][j], scale=sim_std * std[j])
                 for j in xrange(len(train_data[1][0]))]

    new_proj.append(xmin_proj)

    new_data.append(sn_simulator.simulated_der(xmin_proj, epoch))

    ymin_proj = [np.random.normal(loc=train_data[1][indx_ymin][j], scale=sim_std * std[j])
                 for j in xrange(len(train_data[1][0]))]

    new_proj.append(ymin_proj)

    new_data.append(sn_simulator.simulated_der(ymin_proj, epoch))
    

# build array of data
new_proj2 = np.array(new_proj)


# save new data to file
op1 = open('../../data/fake_data.dat', 'w')
for line in new_data:
    for elem in line:
        op1.write(str(elem) + '    ')
    op1.write('\n')
op1.close() 


cut_data = np.array([train_data[1][i] for i in xrange(len(train_data[1])) 
                     if i not in [indx_xmax, indx_xmin, indx_ymin]])


if plot:
    # plot original projections
    plt.figure()
    plt.title('Original projections')
    plt.scatter(cut_data[:,PCx], -cut_data[:,PCy], color='black', marker='x')
    plt.scatter([train_data[1][indx_xmin][PCx]], [-train_data[1][indx_xmin][PCy]], color='blue', marker='o')
    plt.scatter([train_data[1][indx_xmax][PCx]], [-train_data[1][indx_xmax][PCy]], color='red', marker='s')
    plt.scatter([train_data[1][indx_ymin][PCx]], [-train_data[1][indx_ymin][PCy]], color='green', marker='^')
    plt.xlabel('PC' + str(PCx + 1))
    plt.ylabel('PC' + str(PCy + 1))
    plt.show()

    # plot simulated projections
    plt.figure('Extreme points of original + simulation')
    plt.scatter(new_proj2[:,PCx], -new_proj2[:,PCy], color='gray', alpha=0.5, marker='*', label='simulated')
    plt.scatter([train_data[1][indx_xmin][PCx]], [-train_data[1][indx_xmin][PCy]], color='blue', marker='o')
    plt.scatter([train_data[1][indx_xmax][PCx]], [-train_data[1][indx_xmax][PCy]], color='red', marker='s')
    plt.scatter([train_data[1][indx_ymin][PCx]], [-train_data[1][indx_ymin][PCy]], color='green', marker='^')
    plt.legend()
    plt.xlabel('PC' + str(PCx + 1))
    plt.ylabel('PC' + str(PCy + 1))
    plt.show()
