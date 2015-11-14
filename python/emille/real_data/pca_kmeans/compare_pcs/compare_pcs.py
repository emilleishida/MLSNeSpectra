import numpy as np
import pylab as plt


ngroups = 2


# read fluxes
op2 = open('../../type_Ia_max/fluxes_Ia_max.dat', 'r')
lin2 = op2.readlines()
op2.close()

data = [elem.split() for elem in lin2]

fluxes = []
for line in data:
    obj = []
    for item in line:
        obj.append(float(item))
    fluxes.append(obj)

flux_all = np.array(fluxes)   


plt.figure()
plt.suptitle('Mean spectra for ' + str(ngroups) + 'groups, 2 to 9 PCS')

mean_flux = {}

for pcs in xrange(2, 10):
    path1 = '../cl_data/clustering_KMeans_label_' + str(pcs) + 'PC_' + str(ngroups) + 'groups.dat'

    op1 = open(path1, 'r')
    lin1 = op1.readlines()
    op1.close()

    data1 = [elem.split() for elem in lin1]
    data2 = np.array([[float(item) for item in line] for line in data1])

    labels = [int(float(elem.split()[0])) for elem in lin1]

    group_flux = {}
    for key in xrange(max(labels) + 1):
        group_flux[key] = []

    for i in xrange(len(flux_all)):
        group_flux[labels[i]].append(flux_all[i])

    mean_flux[pcs] = {}

    for groups in xrange(max(labels) + 1):
        group_flux[groups] = np.array(group_flux[groups])
        mean_flux[pcs][groups] = [np.mean(group_flux[groups][:,k]) for k in xrange(len(flux_all[0]))]

    
plt.subplot(1,2,1)
plt.title('Group 1')
plt.plot(mean_flux[2][0], label='pc2')
plt.plot(mean_flux[3][1], label='pc3')
plt.plot(mean_flux[4][0], label='pc4')
plt.plot(mean_flux[5][0], label='pc5')
plt.plot(mean_flux[6][0], label='pc6')
plt.plot(mean_flux[7][0], label='pc7')
plt.plot(mean_flux[8][1], label='pc8')
plt.plot(mean_flux[9][1], label='pc9')

plt.subplot(1,2,2)
plt.title('Group 2')
plt.plot(mean_flux[2][1], label='pc2')
plt.plot(mean_flux[3][0], label='pc3')
plt.plot(mean_flux[4][1], label='pc4')
plt.plot(mean_flux[5][1], label='pc5')
plt.plot(mean_flux[6][1], label='pc6')
plt.plot(mean_flux[7][1], label='pc7')
plt.plot(mean_flux[8][0], label='pc8')
plt.plot(mean_flux[9][0], label='pc9')
  
plt.legend()
plt.xlabel('wavelength')
plt.ylabel('fluxes')
plt.show()


            
           

