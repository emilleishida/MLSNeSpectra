path1 = 'hosts_names.txt'
path2 = 'host_only.txt'

op1 = open(path1, 'r')
lin1 = op1.readlines()
op1.close()

data1 = [elem.split() for elem in lin1]

op2 = open(path2, 'w')
for line in data1[1:]:
    if len(line) > 1:
        op2.write(line[-2] + ' ' + line[-1] + '\n')
op2.close

path3 = 'host_coordinates.dat'

op3 = open(path3, 'r')
lin3 = op3.readlines()
op3.close()

data3 = [elem.split() for elem in lin3]

names = [line[0] for line in data3[1:]]

path4 = 'host_only.txt'

op4 = open(path4, 'r')
lin4 = op4.readlines()
op4.close()

data4 = [elem.split()[0] for elem in lin4]

cont = 0
for item in data4:
    if item not in data3:
        cont = cont + 1
        print str(cont) + '. ' +  item

