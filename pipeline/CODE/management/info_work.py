from __future__ import print_function
from name_files import create_name
import os
def prt(OUT_NAME,line,typ='a'):
#	print(line)
	f=open(OUT_NAME,typ)
	print(line,file=f)
	f.close()
sep=' = '
#sep='\t'
def print_info(Method,DICT,HEAD,OUT_NAME,typ='w'):
	f=open(OUT_NAME,typ)
	f.close()
	prt(OUT_NAME,HEAD)
	prt(OUT_NAME,'METHOD'+sep+Method)
	for item in DICT:
		prt(OUT_NAME,item+sep+str(DICT[item]))
	
def read_info(Method,DICT,prefix):
	NAME=create_name(Method,DICT,prefix,info_sufix)
	
