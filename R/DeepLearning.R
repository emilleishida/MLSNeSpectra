
deepLearningSN <- function() {
  
  #path = "C:/CentralRepository/MachineLearning/Projects/PatternsInAstronomy-Physics/CosmoStatistics/ClusteringSN-Spectra/Experiments"
  path = "/home/sasde/documents/COIN_meeting/MLSNeSpectra/R/"
  setwd(path)
  
  ## define libraries
  library(h2o)
  
  ## Read data
  h2oServer <- h2o.init(nthreads=-1)




  TRAIN1     = "../data_all_types/derivatives.dat"
  TRAIN     = "../data_all_types/derivatives.csv"
  dat<-read.table(TRAIN1,header=F,sep='')
  write.csv(dat,TRAIN)

  train.hex <- h2o.importFile(h2oServer, path = TRAIN, header = F, sep = ',', destination_frame="train.hex")
  
  
  ## Construct deep learning model
  dlmodel <- h2o.deeplearning(x=1:148,                        #specify range of columns
                             training_frame = train.hex,      #training filename
                             activation = "Tanh",             #activation function
                             autoencoder=T, 
                             hidden = c(100,50,6), 
                             epochs=100,
                             ignore_const_cols = F)
  
  
  ## Generat new features
  features_dl <- h2o.deepfeatures(dlmodel, train.hex, layer=3)
  head(features_dl)
  
  
  ## Store new features in file
  train_dl <- as.matrix(features_dl)
  write.csv(train_dl, file = "./out_DeepLearning/derivatives_dl.csv", row.names = FALSE)
  
} ## end function
