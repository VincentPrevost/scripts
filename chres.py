import os
import sys
import math

#print(str(sys.argv[1]))
output=str(sys.argv[1])
#xRes=int(input())
xRes=int(sys.argv[2])
#yRes=int(input())
yRes=int(sys.argv[3])
xScaleFact=xRes/1366
yScaleFact= yRes/768

cmd='xrandr --output '+ output + ' --scale ' + str(xScaleFact) + 'x' + str(xScaleFact) + ' --panning ' + str(xRes) + 'x' + str(yRes)
print(cmd)
os.system(cmd)
