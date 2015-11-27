from rpy2.robjects import r
import numpy as np

def reduction(data, params):

	in_param	= ''
    # parse parameters

	for item in params:
	    if isinstance(params[item], str):
	        in_param += ', '+item+' = '+params[item]
	    else:
	        exec(item+'='+str(params[item]))

    # apply PCA

	
	size_data 	= np.shape(data)[1]
	in_param	= 'x=1:%d'%(size_data) + ''.join([ ', '+item+' = '+params[item] for item in params if isinstance(params[item], str)])

	print('training_frame = train.hex, activation = "Tanh", autoencoder = T, hidden = c(120,60,30), epochs = 100, ignore_const_cols = F')
	print('')
	print(in_param[9:])
	print(in_param)
	print('\n')
	
	
	in_file_cvs='./.temp_file.cvs'
	np.savetxt(in_file_cvs, data, delimiter=',', fmt='%.18f')
	
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

	return X
