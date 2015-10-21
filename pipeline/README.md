# Pipeline for the use of data reduction and clustering

## Basic use
To run the whole pipeline execute:

	./ALL

To just the reduction part execute:

	./REDUCTION

To just the clustering execute:

	./CLUSTERING

All cases are configured by:

	config.py

## Outputs
The outputs of reduction methods are placed in **red_data/**.
The outputs of clustering methods are placed in **plots/**

## Adding your code
If you want to add your code to the pipeline, put it in the one of the following dirs and we will format it for you:

	EXTERNAL_CODES/clustering/
	EXTERNAL_CODES/reduction/
