import os
mylist = os.listdir(os.getcwd())
new = []
for one in mylist:
    if 'zip' not in one:
        new.append(one)

for one in new:
    if one != 'delete.py':
        _path = os.path.join(os.getcwd(),one)
            
        sonPath = os.path.join(_path)
        fsize = os.path.getsize(sonPath)
        
        f_kb = fsize/float(1024)
        # print(sonPath,f_kb)
        if f_kb > 5:
            print(sonPath)
            cmd = 'rm '+sonPath
            os.popen("sudo -S %s"%(cmd), 'w').write('lywh978216-')
    else:
        continue