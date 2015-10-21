from __future__ import print_function
from config import *

def update_dict(DICT,prefix):
	for item0 in DICT:
		item=prefix+item0
		try:
			exec(item)
		except NameError:
			pass
		else:
  			print (item0,"\t was updated from",DICT[item0],"to",eval(item))
			DICT[item0]=eval(item)
			

