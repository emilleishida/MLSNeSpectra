#!/bin/bash

cd create_data; python select_data.py ; cd ../

cd empca; python plot_data.py; python run_empca.py & cd ../
cd pca; python plot_data.py; python run_pca.py & cd ../
cd kpca; python kpca.py & cd ../


