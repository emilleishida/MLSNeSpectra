path1 = '../../../../data_all_types/derivatives.dat'
path2 = '../../../../data_all_types/labels.dat'
path3 = 'data_Ia_max.dat'
path4 = '../../../../data_all_types/fluxes.dat'
path5 = 'fluxes_Ia_max.dat'

op1 = open(path1, 'r')
lin1 = op1.readlines()
op1.close()

op4 = open(path4, 'r')
lin4 = op4.readlines()
op4.close()

op2 = open(path2, 'r')
lin2 = op2.readlines()
op2.close()

labels = [elem.split()[0] for elem in lin2]

op3 = open(path3, 'w')
op5 = open(path5, 'w')
for i in xrange(len(labels)):
    if float(labels[i]) == 1.0:
        op3.write(lin1[i])
        op5.write(lin4[i])
op3.close()
op5.close()


