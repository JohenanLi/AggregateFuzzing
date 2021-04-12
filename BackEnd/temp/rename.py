import os
allFiles = os.listdir(os.getcwd())
newFile = []
for one in allFiles:
    if 'mini' in one:
        newFile.append(one)
for one in newFile:
    # print(one[12:])
    cmd = 'mv {} {}'.format(one,one[12:])
    os.system(cmd)