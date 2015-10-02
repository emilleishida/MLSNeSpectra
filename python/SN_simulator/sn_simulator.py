
import numpy as np
import pickle

empca_dict_file = './trained_empca.dict'

range_out = [14,372]

def simulated_der(sn_coeff, epoch):
    r"""
    It creates the derivative of an object with coefficients "sn_coeff".
    sn_coeff has to be a 5 element list of coefficients.
    epoch needs to be within -12.5 and +17.2 days.

    e.g.:
    derivative = simulated_der(sn_coeff=[-0.047, 0.023, -0.038, 0.011, 0.019], epoch=3.)

    """
    filehandler = open(empca_dict_file, 'r')
    empca_dict = pickle.load(filehandler)
    filehandler.close()
    mean_derivative = empca_dict['mean_derivative']
    eigvec = empca_dict['eigvec']
    reconstruct_deriv = np.sum(eigvec.T*sn_coeff,1)+mean_derivative
    bins = empca_dict['bins']
    wave_range = empca_dict['wave_range']
    for j in range(np.size(bins[:-1])):
        if bins[j] <= epoch and epoch < bins[j+1]:
            range_0 = np.size(reconstruct_deriv)/(np.size(bins)-1)
            return (reconstruct_deriv[range_0*j:range_0*(j+1)])[range_out[0]:range_out[1]]
    return None

def load_training_coeff(pkl_file='./training_coeff.pkl'):
    r"""
    It loads the training coefficients and names from the pkl file.
    """
    # load training sample coeff
    filehandler = open(pkl_file, 'r')
    training_sne, training_coeff = pickle.load(filehandler)
    filehandler.close()
    return training_sne, training_coeff

def random_generator(return_derivative=True,epoch=0.):
    import random
    r"""
    It generates the derivative of a random SN. The distribution is similar to
    the distribution of the training set. 
    Set "return_derivative=False" to return the random coefficients instead of 
    the derivative.
    "epoch" is the epoch to use.
    """
    sigma_ratio=0.3
    training_sne, training_coeff = load_training_coeff()
    sn_n = random.randint(0,np.size(training_sne)-1)
    rand_coeff=[]
    for i in range(np.size(training_coeff[0])):
        sigma = sigma_ratio*np.sqrt(np.var(training_coeff.T[i]))
        rand_coeff.append(random.gauss(training_coeff[sn_n][i], sigma=sigma))
    if return_derivative:
        return simulated_der(rand_coeff, epoch)
    else:
        return rand_coeff

