import urllib
import numpy

path1 = 'https://iopscience.iop.org/1538-3881/143/5/126/suppdata/aj427309t4_mrt.txt'
op1 = urllib.urlopen(path1, 'r')


lin1 = op1.readlines()
op1.close()
#data1 = [elem[17:].split() for elem in lin1[51:]]
data1 = [elem[:16].split()[0] for elem in lin1[51:]]
data2 = [elem[41:].split() for elem in lin1[51:]]

for i in range(numpy.shape(data2)[0]):
    if numpy.size(data2[i])==1:
        data2[i]= [ data2[i][0],'nan']






