# commit that is working 5cc26aa8e5918759e17afa0bdf340b1faf805d2d


ngroups = 11
ncomp = 3

"""
for k in xrange(2, ngroups):
    op3 = open(str(k) + '_groups/config.py', 'r')
    lin3 = op3.readlines()
    op3.close()

    data3 = [elem.split() for elem in lin3]

    op4 = open(str(k) + '_groups/config.py', 'w')
    for item in data3:
        if len(item) > 1 and item[0] == 'pca_n_components':
            for elem in item[:-1]:
                op4.write(elem + '    ')
            op4.write(str(ncomp) + '\n')
            
        else:
            for elem in item:
                op4.write(elem + '    ')
            op4.write('\n')
    op4.close()    
            
"""


results = {}
results['silhouette'] = []
results['Dunn_index'] = []
results['DavisBouldin_index'] = []
results['vrc'] = []


for i in xrange(2, ngroups):
    op1 = open(str(i) + '_groups/info/quality.info', 'r')
    lin1 = op1.readlines()
    op1.close()

    data1 = [elem.split() for elem in lin1]

    results['silhouette'].append(float(data1[41][-1]))
    results['Dunn_index'].append(float(data1[42][-1]))
    results['DavisBouldin_index'].append(float(data1[43][-1]))
    results['vrc'].append(float(data1[44][-1]))
   

op2 = open('summary_quality_' + str(ncomp) + 'PC.dat', 'w')
op2.write('n_groups \t silhouette \t Dunn \t \t \t Davis \t \t \t vrc\n')
for j in xrange(ngroups - 2):
    op2.write(str(j + 2) + '\t \t \t' + str(results['silhouette'][j]) + '\t' + str(results['Dunn_index'][j]) + '\t' + str(results['DavisBouldin_index'][j]) + '\t' + str(results['vrc'][j]) + '\n')

op2.write('\n Final results \n')

op2.write('        \t silhouette \t Dunn \t Davis \t vrc\n')
op2.write('n_groups \t \t \t \t' + str(results['silhouette'].index(max(results['silhouette'])) + 2) + '\t \t' + \
                         str(results['Dunn_index'].index(max(results['Dunn_index'])) + 2) + '\t \t' + \
                         str(results['DavisBouldin_index'].index(min(results['DavisBouldin_index'])) + 2) + '\t \t' + \
                         str(results['vrc'].index(min(results['vrc'])) + 2))
op2.close()

