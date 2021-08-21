from subprocess import getoutput
dir = "/root/AggregateFuzzing/BackEnd/sourceTotal/ImageMagick"
a = getoutput("find %s -name CMakeLists.txt"%(dir))
print(a == "")
