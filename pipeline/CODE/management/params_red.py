from __future__ import print_function
pca_dict=dict([
	[ 'n_components'	, 6	],
])

empca_dict=dict([
	[ 'errors_file'	        , None	],
	[ 'n_components'	, 6			],
        [ 'smooth'	        , 0			],
	[ 'n_iter'	        , 50			],
])

deeplearning_dict=dict([
	[ 'n_layers'		, 3		],
	[ 'training_frame'	, 'train.hex'	],
	[ 'activation'		, '"Tanh"'	],
	[ 'autoencoder'		, 'T'		],
	[ 'hidden'		, 'c(120,30,60)'],
	[ 'epochs'		, '100'		],
	[ 'ignore_const_cols'	, 'F'		],
])
