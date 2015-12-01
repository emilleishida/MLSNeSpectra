
import numpy as np
from sklearn.decomposition.pca import PCA
from numpy import loadtxt, genfromtxt, savetxt, var, random
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim

#data_dir='../../data/'
data_dir='../../data_all_types/'
out_dir='./plots/'

# load the data and run PCA
derivatives = loadtxt(data_dir+'derivatives.dat')
labels = loadtxt(data_dir+'labels.dat')
spectra_data = genfromtxt(data_dir+'spectra_data.dat',dtype=None)

random.seed(2)

sne_names= set(spectra_data['f0']) # one entry for each SN
train_names=[]
for sn in sne_names:
    if random.random() > .20:
        train_names.append(sn)


train_mask=[]
#train_mask_no_TL=[]
test_mask=[]
for i in range(np.size(labels)):
    #if labels[i]==1:
    if spectra_data['f0'][i] in train_names:
        train_mask.append(i)
        #train_mask_no_TL.append(i)
    else:
        test_mask.append(i)
    #if labels[i]==0:
    #    #if spectra_data['f0'][i] in train_names:
    #    train_mask_TL.append(i)
        


#######################################################
#   To run the DL.
from rpy2.robjects import r
def DL( train, test, n ):

    input_string = '120,100,90,50,30,20,%d,20,30,50,90,100,120' % (n)
    seed = 1
    in_param = 'training_frame = train3.hex, activation = "Tanh", autoencoder=T, hidden = c(%s), epochs=100, ignore_const_cols = F, seed = %d '  % (input_string,seed)
    n_layers = 7
    size_in_data = np.shape(train)[1]
    in_param = 'x=1:%d,' % (size_in_data) + in_param
    in_file_cvs='./.temp_file.cvs'
    np.savetxt(in_file_cvs, train, delimiter=',', fmt='%.18f')
    ## define libraries
    r('library(h2o)')
    ## Read data
    r('h2oServer <- h2o.init(nthreads=-1)')
    r('TRAIN = "%s" '% (in_file_cvs))
    r('train3.hex <- h2o.importFile(h2oServer, path = TRAIN, header = F, sep = ",", destination_frame="train3.hex")')
    ## Construct deep learning model
    r('dlmodel <- h2o.deeplearning( %s ) ' % (in_param))
    ## Generate new features
    r('features_dl <- h2o.deepfeatures(dlmodel, train3.hex, layer=%d)' % (n_layers))
    r('head(features_dl)')
    ## new features
    X = r('as.matrix(features_dl)')




    in_file_cvs='./.temp_file.cvs'
    np.savetxt(in_file_cvs, test, delimiter=',', fmt='%.18f')
    ## Read data
    r('h2oServer <- h2o.init(nthreads=-1)')
    r('TEST = "%s" '% (in_file_cvs))
    r('test3.hex <- h2o.importFile(h2oServer, path = TEST, header = F, sep = ",", destination_frame="test3.hex")')
    ## Generate predictions
    r('predictions_dl <- h2o.predict(dlmodel, test3.hex)')
    r('head(predictions_dl)')
    ## new predictions
    pred = r('as.matrix(predictions_dl)')
    return var(pred -test)
################################################################

figure()
variances_table = []

for i in range(2,26,1):
    pca = PCA(n_components=i)
    der = derivatives[train_mask]
    pca.fit(der)
    X = pca.transform(derivatives[test_mask])
    pred_pca_temp = (pca.inverse_transform(X))

    #
    var_fraction_pca = var(pred_pca_temp-derivatives[test_mask])/var(derivatives[test_mask])
    #plot([i], [var(pred_pca_temp-derivatives[test_mask])],'D')

    var_fraction_DL = DL( derivatives[train_mask], derivatives[test_mask], i)/var(derivatives[test_mask])
    #var_fraction_DL = 0

    #plot([i], [var_DL_TL ],'Dk')

    #pca = PCA(n_components=i)
    #der = derivatives[train_mask_no_TL]
    #pca.fit(der)
    #X = pca.transform(derivatives[test_mask])
    #pred_pca_temp = (pca.inverse_transform(X))

    #var_fraction_pca_no_TL = var(pred_pca_temp-derivatives[test_mask])/var(derivatives[test_mask])
    ##plot([i], [var(pred_pca_temp-derivatives[test_mask])],'x')

    #var_fraction_DL_no_TL = DL( derivatives[train_mask_no_TL], derivatives[test_mask], i)/var(derivatives[test_mask])
    ##plot([i], [var_DL_no_TL ],'xk')


    variances_table.append([i,var_fraction_pca, var_fraction_DL]) #, var_fraction_DL_no, var_fraction_DL])

savetxt('./residuals_all_matrix.dat', variances_table, header='nPCs fraction_variance_PCA fraction_variance_DL'   )



data_to_plot = loadtxt('./residuals_all_matrix.dat').T
figure()
plot(data_to_plot[0], data_to_plot[1],'or')
plot(data_to_plot[0], data_to_plot[2],'ok')
