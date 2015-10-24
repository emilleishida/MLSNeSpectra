#!/bin/bash

cd /home/emille/Documents/github/mlsnespectra/MLSNeSpectra/python/emille/simulations/pca_kmeans/0/

for dir in `ls -d */`; do cd $dir ; ALL; cd ..; done
