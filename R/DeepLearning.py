from rpy2.robjects import r
import numpy as np

#in_file = "../data_all_types/derivatives_train.dat"
in_file = "../data_all_types/derivatives.dat"

for input_string in '120,100,90,50,30,20,2,20,30,50,90,100,120', '120,100,90,50,30,20,3,20,30,50,90,100,120', '120,100,90,50,30,20,4,20,30,50,90,100,120', '120,100,90,50,30,20,5,20,30,50,90,100,120', '120,100,90,50,30,20,6,20,30,50,90,100,120', '120,100,90,50,30,20,7,20,30,50,90,100,120', '120,100,90,50,30,20,8,20,30,50,90,100,120', '120,100,90,50,30,20,9,20,30,50,90,100,120':
    #for input_string in ['120,100,90,50,30,20,2,20,30,50,90,100,120']:
    #for seed in [1,2,3,4,5,6]:
    seed = 1
    #input_string = '120,100,90,50,30,20,2,20,30,50,90,100,120'

    #for input_string in ['100,50,2,50,100']:
    #for input_string in ['120,100,90,50,30,20,5,2,5,20,30,50,90,100,120']:
    
    in_param = 'training_frame = train2.hex, activation = "Tanh", autoencoder=T, hidden = c(%s), epochs=100, ignore_const_cols = F, seed = %d, reproducible = TRUE '  % (input_string,seed)
    #in_param = 'training_frame = train.hex, activation = "Tanh", autoencoder=T, hidden = c(120,100,90,50,30,20,10,20,30,50,90,100,120), epochs=100, ignore_const_cols = F'  
    n_layers = 7
    #n_layers = 3
    #in_param = 'training_frame = train.hex, activation = "Tanh", autoencoder=T, hidden = c(180,120,100,90,70,50,40,30,20,10,20,30,40,50,70,90,100,120,180), epochs=300, ignore_const_cols = F'  
    #n_layers = 10
    
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
    
    r('train2.hex <- h2o.importFile(h2oServer, path = TRAIN, header = F, sep = ",", destination_frame="train2.hex")')
    
    ## Construct deep learning model
    r('dlmodel <- h2o.deeplearning( %s ) ' % (in_param))
    
    ## Generate new features
    r('features_dl <- h2o.deepfeatures(dlmodel, train2.hex, layer=%d)' % (n_layers))
    r('head(features_dl)')
    
    ## Store new features in file
    X = r('as.matrix(features_dl)')
    np.savetxt('./out_DeepLearning/out_%s_seed%d_dl.dat' % (input_string,seed)  ,X)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    in_file = "../data_all_types/derivatives.dat"
    #in_file = "../data_all_types/derivatives_test.dat"
    
    in_data = np.loadtxt(in_file)
    
    in_file_cvs='./.temp_file.cvs'
    np.savetxt(in_file_cvs, in_data, delimiter=',', fmt='%.18f')
    
    ## Read data
    r('h2oServer <- h2o.init(nthreads=-1)')
    
    r('TEST = "%s" '% (in_file_cvs))
    
    r('test.hex <- h2o.importFile(h2oServer, path = TEST, header = F, sep = ",", destination_frame="test.hex")')
    
    ## Generate predictions
    r('predictions_dl <- h2o.predict(dlmodel, test.hex)')
    r('head(predictions_dl)')
    
    ## Store new predictions in file
    pred = r('as.matrix(predictions_dl)')
    np.savetxt('./out_DeepLearning/predictions_%s_seed%d_dl.dat' % (input_string,seed) ,pred)

  
