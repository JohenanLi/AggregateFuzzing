from os import listdir,path,system
import sys
def delDuplicate(dir):
    a = listdir(dir)
    tstDict = {}
    for one in a:
        temp = path.splitext(one)[-1]
        if temp == "":
            continue
        if tstDict.get(temp) == None:
            tstDict[temp] = 0
        else:
            tstDict[temp] += 1

    maxVal = -1
    curExt = ""
    for (key,value) in tstDict.items():
        if value > maxVal:
            maxVal = value
            curExt = key
        else:
            continue

    if maxVal > 10:
        system("rm *%s"%(curExt))
        print("删除%s"%(curExt))



if __name__ == "__main__":
    if sys.argv[1] == "-d":
        delDuplicate(sys.argv[2])