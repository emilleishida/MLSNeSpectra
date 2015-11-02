import numpy as np

path1 = 'summary.dat'

op2 = open(path1, 'w')
op2.write('comp \t silhouette \t dunn \t davis \t vrc \n')

silhouette = {}
dunn = {}
davis = {}
vrc = {}
clusters = {}

for pcs in range(2, 10):
    op1 = open(str(pcs) + 'comp/info/quality.info', 'r')
    lin1 = op1.readlines()
    op1.close()
    data1 = [elem.split() for elem in lin1]

    op2.write(str(pcs) + ' \t ' + data1[-4][-1] + ' \t ' + data1[-3][-1] + ' \t ' + data1[-2][-1] + ' \t ' + data1[-1][-1] + '\n')

    silhouette[str(pcs) + 'PC'] = float(data1[-4][-1])
    dunn[str(pcs) + 'PC'] = float(data1[-3][-1])
    davis[str(pcs) + 'PC'] = float(data1[-2][-1])
    vrc[str(pcs) + 'PC'] = float(data1[-1][-1])

    for line in data1:
        if len(line) > 1 and line[0] == 'n_clusters':
            clusters[str(pcs) + 'PC'] = line[-1]
            break

max_silhouette = max(silhouette.values())
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

min_vrc = min(vrc.values())
for key in vrc.keys():
    if vrc[key] == min_vrc:
        result_vrc = key
        break

op2.write('\n\n')
op2.write('*** Final results ****\n\n')
op2.write('Silhouette \t' + str(max_silhouette) + ' \t ' + result_silhouette + ' \t ' + clusters[result_silhouette] + '\n')
op2.write('Dunn \t' + str(max_dunn) + ' \t ' + result_dunn + ' \t ' + clusters[result_dunn] + '\n')
op2.write('Davis  \t' + str(min_davis) + ' \t ' + result_davis + ' \t ' + clusters[result_davis] + '\n')
op2.write('vrc \t' + str(min_vrc) + ' \t ' + result_vrc + ' \t ' + clusters[result_vrc] + '\n')
op2.close()


