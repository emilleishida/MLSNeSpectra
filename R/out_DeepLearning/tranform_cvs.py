import numpy
import glob
data_dir ='./'

SNe_spectra= glob.glob(data_dir+'*.csv')
for name in SNe_spectra:
   print name
   in_cvs = numpy.genfromtxt(name,delimiter=',',skip_header=1)
   numpy.savetxt(name[:-4]+'.dat', in_cvs)
