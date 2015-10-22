# Pipeline for the use of data reduction and clustering
Pipeline to use all methods of data reduction and clustering.
So far we have implemented:

* For data reduction:
	* PCA
* For clustering
	* MeanShift
	* KMeans
	* AffinityPropagation
	* AgglomerativeClustering
	* DBSCAN

## Basic use
The idea of the code is to get the function of the pipeline and 
run the code in a outside dir. You should first prepare your environment with these simple steps.

### Prepare environment
It is very easy to prepare your environment to run the pipeline.
It can be done in 2 steps:

Get the nice functions we prepared. In the pipeline dir, do the command:

	source SOURCE_ME

Create your own dir (preferably outside the pipeline dir) to run the code and copy the config.py file there:

	mkdir your_dir
	cd your_dir
	cp PIPELINE_DIR/example_config.py config.py

Now you are ready to run the pipeline functions!

### Pipeline function
Inside your own working dir with the config.py file you can use any of these functions:

To run the whole pipeline execute:

	ALL

To just the reduction part execute:

	REDUCTION

To just the clustering execute:

	CLUSTERING

Remeber, all cases are configured by:

	config.py

## Outputs
The outputs of reduction methods are placed in **red_data/**.
The outputs of clustering methods are placed in **plots/**

## Adding your code
If you want to add your code to the pipeline, put it in the one of the following dirs inside the pipeline and we will format it for you:

	EXTERNAL_CODES/clustering/
	EXTERNAL_CODES/reduction/
