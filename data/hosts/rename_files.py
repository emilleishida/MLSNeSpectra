import os

# read host name and fiber, plate, mjd connection
path1 = 'List_SDSS.csv'

op1 = open(path1, 'r')
lin1 = op1.readlines()
op1.close()


# create dictionary for host name and fiber, plate, mjd connection
data1 = [elem.split(',') for elem in lin1]
host_sdssid = {}
for line in data1[1:]:
    if len(line[-2]) > 0 and len(line[-3]) == 4 and len(line[-1][:-1]) == 4:
        host_sdssid[line[1]] = line[-3] + '-' + line[-2] + '-' + line[-1][:-1]
    elif len(line[-2]) > 0 and len(line[-3]) == 3 and len(line[-1][:-1]) == 4:
        host_sdssid[line[1]] = '0' + line[-3] + '-' + line[-2] + '-' + line[-1][:-1]
    elif len(line[-2]) > 0 and len(line[-3]) == 2 and len(line[-1][:-1]) == 4:
        host_sdssid[line[1]] = '00' + line[-3] + '-' + line[-2] + '-' + line[-1][:-1]
    elif len(line[-2]) > 0 and len(line[-3]) == 4 and len(line[-1][:-1]) == 3:
        host_sdssid[line[1]] = line[-3] + '-' + line[-2] + '-0' + line[-1][:-1]
    elif len(line[-2]) > 0 and len(line[-3]) == 4 and len(line[-1][:-1]) == 2:
        host_sdssid[line[1]] = line[-3] + '-' + line[-2] + '-00' + line[-1][:-1]
    elif len(line[-2]) > 0 and len(line[-3]) == 3 and len(line[-1][:-1]) == 3:
        host_sdssid[line[1]] = '0' + line[-3] + '-' + line[-2] + '-0' + line[-1][:-1]


# read host sn name connection
path2 = 'hosts_names.txt'

op2 = open(path2, 'r')
lin2 = op2.readlines()
op2.close()

data2 = [elem.split() for elem in lin2]

# create dictionary for host sn connection
sn_host = {}
for line in data2[1:]:
   if len(line) > 2:
       sn_host[line[-1]] = line[0]


# rename files using sn name connection
host_done = []
for key in host_sdssid.keys():

    print key + ' - ' + host_sdssid[key]

    if os.path.isfile('specs_orig/' + host_sdssid[key] + '.cxt'):

        op3 = open('specs_orig/' + host_sdssid[key] + '.cxt', 'r')
        lin3 = op3.readlines()
        op3.close()

        data3 = [elem.split() for elem in lin3]

        op4 = open('specs_renamed/' + sn_host[key] + '_g' + key + '.dat', 'w')
        for line in data3:
            for j in xrange(3):
                op4.write(line[j] + '    ')
            op4.write('\n')
        op4.close()

        host_done.append(key)

# print missing hosts
op5 = open('missing_hosts.dat', 'w')
for key in sn_host.keys():
    if key not in host_done:
        op5.write(sn_host[key] + '    ' + key + '\n')
op5.close()    



