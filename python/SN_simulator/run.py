import sn_simulator
import pylab as plt

train_data = sn_simulator.load_training_coeff()





plt.figure()
plt.scatter(train_data[1][:,0], -train_data[1][:,1])
plt.show()
