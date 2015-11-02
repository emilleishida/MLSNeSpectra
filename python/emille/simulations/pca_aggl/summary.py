real_groups = [2, 3, 3, 1, 3, 4, 4]

op3 = open('summary_quality.dat', 'w')
op3.write('***************************************\n')

for sim in xrange(7):
    path1 = str(sim) + '/summary.dat'

    op2 = open(path1, 'w')
    op2.write('PCS \t groups \t silhouette \t dunn \t davis \t vrc \n')


    silhouette = {}
    dunn = {}
    davis = {}
    vrc = {}

    for pcs in range(2, 5):
        for groups in range(2, 9):
            op1 = open(str(sim) + '/' + str(pcs) + 'PC/info/quality_' + str(groups) + 'groups.info', 'r')
            lin1 = op1.readlines()
            op1.close()

            data1 = [elem.split() for elem in lin1]
 
            op2.write(str(pcs) + ' \t ' + str(groups) + ' \t ' + data1[-4][-1] + ' \t ' + data1[-3][-1] + ' \t ' + data1[-2][-1] + ' \t ' + data1[-1][-1] + '\n')

            silhouette[str(pcs) + 'PC_' + str(groups) + 'g'] = float(data1[-4][-1])
            dunn[str(pcs) + 'PC_' + str(groups) + 'g'] = float(data1[-3][-1])
            davis[str(pcs) + 'PC_' + str(groups) + 'g'] = float(data1[-2][-1])
            vrc[str(pcs) + 'PC_' + str(groups) + 'g'] = float(data1[-1][-1])

        

    max_silhouette = max(silhouette.values())
    for key in silhouette.keys():
        if silhouette[key] == max_silhouette:
            result_silhouette = key
            break

    max_dunn = max(dunn.values())
    for key in dunn.keys():
        if dunn[key] == max_dunn:
            result_dunn = key
            break

    min_davis = min(davis.values())
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
    op2.write('Silhouette \t' + str(max_silhouette) + ' \t ' + result_silhouette + '\n')
    op2.write('Dunn \t' + str(max_dunn) + ' \t ' + result_dunn + '\n')
    op2.write('Davis  \t' + str(min_davis) + ' \t ' + result_davis + '\n')
    op2.write('vrc \t' + str(min_vrc) + ' \t ' + result_vrc + '\n')

    op2.close()

    op3.write('Simulation ' + str(sim) + '  - ' + str(real_groups[sim]) + ' groups\n\n')
    op3.write('Silhouette \t' + str(max_silhouette) + ' \t ' + result_silhouette + '\n')
    op3.write('Dunn \t' + str(max_dunn) + ' \t ' + result_dunn + '\n')
    op3.write('Davis  \t' + str(min_davis) + ' \t ' + result_davis + '\n')
    op3.write('vrc \t' + str(min_vrc) + ' \t ' + result_vrc + '\n\n')
    op3.write('***************************************\n')

op3.close()
    
