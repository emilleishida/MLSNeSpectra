import os
import tarfile



url_tar = "https://www.dropbox.com/s/q22paf70tyulvka/derivatives.dat.tgz?dl=0"



# load the data and run PCA

if "derivatives.dat" not in os.listdir("./"):
	
	os.system( "wget %s"%url_tar )
	
	os.system( "tar -xzf derivatives.dat.tgz*")
	os.system( "rm derivatives.dat.tgz?dl=0" )
