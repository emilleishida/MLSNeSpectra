from rpy2.robjects import r
import numpy as np

in_file = "../data_all_types/derivatives.dat"

in_param = 'training_frame = train.hex, activation = "Tanh", autoencoder=T, hidden = c(120,60,30), epochs=100, ignore_const_cols = F'  
n_layers = 3

in_data = np.loadtxt(in_file)
size_in_data = np.shape(in_data)[1]

in_param = 'x=1:%d,' % (size_in_data) + in_param

in_file_cvs='./.temp_file.cvs'
np.savetxt(in_file_cvs, in_data, delimiter=',', fmt='%.18f')

## define libraries
r('library(h2o)')
  
## Read data
r('h2oServer <- h2o.init(nthreads=-1)')

r('TRAIN = "%s" '% (in_file_cvs))

r('train.hex <- h2o.importFile(h2oServer, path = TRAIN, header = F, sep = ",", destination_frame="train.hex")')

## Construct deep learning model
r('dlmodel <- h2o.deeplearning( %s ) ' % (in_param))

## Generate new features
r('features_dl <- h2o.deepfeatures(dlmodel, train.hex, layer=%d)' % (n_layers))
r('head(features_dl)')

## Store new features in file
X = r('as.matrix(features_dl)')
np.savetxt('./out_DeepLearning/derivatives_dl.dat',X)



## Generate predictions
r('predictions_dl <- h2o.predict(dlmodel, train.hex)')
r('head(predictions_dl)')

## Store new predictions in file
pred = r('as.matrix(predictions_dl)')
np.savetxt('./out_DeepLearning/predictions_dl.dat',pred)

  
