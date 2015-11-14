import numpy as np
path1 = 'summary.dat'

op2 = open(path1, 'w')
op2.write('groups \t quantile  \t silhouette \t dunn \t davis \t vrc \n')


silhouette = {}
dunn = {}
davis = {}
vrc = {}

l1 = np.arange(0.01, 0.21, 0.01)
l2 = list(l1)
l2.insert(0, 0.25)

for quantiles in l2:
    print quantiles
    if str(quantiles) == '0.1':
        op1 = open('par_0.10/info/quality.info', 'r')
    elif str(quantiles) == '0.2':
        op1 = open('par_0.20/info/quality.info', 'r')
    else:
        op1 = open('par_' + str(round(float(quantiles),2)) + '/info/quality.info', 'r')
    lin1 = op1.readlines()
    op1.close()

    data1 = [elem.split() for elem in lin1]

    op2.write(data1[-26][-1] + '\t'  + '\t' + str(quantiles) + ' \t ' + data1[-4][-1] + ' \t ' + data1[-3][-1] + ' \t ' + data1[-2][-1] + ' \t ' + data1[-1][-1] + '\n')

    silhouette[str(quantiles) + 'q' + data1[-26][-1] + 'g'] = float(data1[-4][-1])
    dunn[str(quantiles) + 'q' + data1[-26][-1] + 'g'] = float(data1[-3][-1])
    davis[ str(quantiles) + 'q' + data1[-26][-1] + 'g'] = float(data1[-2][-1])
    vrc[str(quantiles) + 'q' + data1[-26][-1] + 'g'] = float(data1[-1][-1])

        

max_silhouette = np.nanmax(silhouette.values())
for key in silhouette.keys():
    if silhouette[key] == max_silhouette:
        result_silhouette = key
        break

max_dunn = np.nanmax(dunn.values())
for key in dunn.keys():
    if dunn[key] == max_dunn:
        result_dunn = key
        break

min_davis = np.nanmin(davis.values())
for key in davis.keys():
    if davis[key] == min_davis:
        result_davis = key
        break

min_vrc = np.nanmin(vrc.values())
for key in vrc.keys():
    if vrc[key] == min_vrc:
        result_vrc = key
        break

op2.write('\n\n')
op2.write('*** Final results ****\n\n')
op2.write('Silhouette \t' + str(max_silhouette) + ' \t ' + result_silhouette + '\n')
op2.write('Dunn \t' + str(max_dunn) + ' \t ' + result_dunn + '\n')
op2.write('Davis  \t' + str(min_davis) + ' \t ' + result_davis + '\n')
op2.write('vrc \t' + str(min_vrc) + ' \t ' + result_vrc + '\n')

op2.close()
