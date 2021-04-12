import os,sys
print(sys.path)
names = []
with open('aaa.txt','r') as f:
    names = f.readlines()
f.close()
dirName = []
with open('seed.txt','r') as f:
    dirName = f.readlines()
f.close()
#cmd = 'sudo unzip -d {} {}'.format('/'+dirName[0],names[0])
# cmd = 'sudo unzip {}'.format(names[0].strip())
# os.popen("sudo -S %s"%(cmd), 'w').write('lywh978216-')
for i in range(len(names)):
    cmd = 'sudo unzip {}'.format(names[i].strip())
    os.popen("sudo -S %s"%(cmd), 'w').write('lywh978216-')