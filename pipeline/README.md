# Pipeline for the use of data reduction and clustering
Pipeline to use all methods of data reduction and clustering.
So far we have implemented:

* For data reduction:
	* PCA
	* empca
* For clustering
	* MeanShift
	* KMeans
	* AffinityPropagation
	* AgglomerativeClustering
	* DBSCAN

## Requirements
To run fully this pipeline, you will need:

	numpy
	matplotlib
	sklearn

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

To just the ploting execute:

	PLOT

Remeber, all cases are configured by:

	config.py

## Outputs
The outputs of reduction methods are placed in **red_data/**.
They will be input for clustering and plotting unless stated otherwise.

The outputs of clustering methods are placed in **cl_data/**.
They will be input for plotting unless stated otherwise.

The outputs of plotting are placed in **plots/**.

## Adding your code
If you want to add your code to the pipeline, put it in the one of the following dirs inside the pipeline and we will format it for you:

	EXTERNAL_CODES/clustering/
	EXTERNAL_CODES/reduction/

## Sharing plots
If you want to share plots done with (or without) the pipeline,
put them in

	share_plots/

Please mind the name of your plots so you don't overwrite other peoples results.

## Advanced plotting
The default plotting results in a figure (.png) with all the PCs colored according to the clusters.
If you want to change the extension of the figure or the color arrangement,
change the parameters in the config file (see HOW_TO_USE_CONFIG README).

If you want other options, there are a few available using keys in the terminal when executing the **PLOT** command.
Here are the plossibilities:

	-nd	(or --no_diag	) : do not plot diagonal
	-nf	(or --no_fit	) : do not fit in all dimensions simultanniously
	-nc	(or --no_colors	) : do not use colors
	-nl	(or --no_label	) : do not plot label
	-w	(or --window	) : keep plot in interactive window, this will not save the output automaticaly
	-pp	(or --plot_pars	) : plot specified pars, takes a string as input (ex: "1 2")
	-hs	(or --horiz_space) : set horizontal spacing between the plots
	-vs	(or --vert_space) : set vertical spacing between the plots

You can also see them by executing

	PLOT -h

