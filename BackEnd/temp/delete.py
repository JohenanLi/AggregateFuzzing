import os
mylist = os.listdir(os.getcwd())
new = []
for one in mylist:
    if 'zip' not in one:
        new.append(one)
print(new,len(new))
for one in new:
    _path = os.path.join(os.getcwd(),one)
    sonList = os.listdir(_path)
    print(one)
    if one == 'xpm':
        print(sonList)
    for son in sonList:
        
        sonPath = os.path.join(_path,son)
        fsize = os.path.getsize(sonPath)
        
        f_kb = fsize/float(1024)
        # print(sonPath,f_kb)
        if f_kb > 5:
            print(sonPath)
            cmd = 'rm '+sonPath
            os.popen("sudo -S %s"%(cmd), 'w').write('lywh978216-')