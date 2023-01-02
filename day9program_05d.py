def printday(dn):
    mn=''
    if(dn==1):
        mn= 'monday'
    elif(dn==2):
        mn= 'tuesday'
    elif(dn==3):
        mn= 'wednesday'
    elif(dn==4):
        mn= 'thursday'
    elif(dn==5):
        mn= 'friday'
    elif(dn==6):
        mn= 'sat'
    elif(dn==7):
        mn= 'sun'
   
    return mn


def printday1(dn):
    mn=''
    if(dn==1):
        mn= 'monday'
    if(dn==2):
        mn= 'tuesday'
    if(dn==3):
        mn= 'wednesday'
    if(dn==4):
        mn= 'thursday'
    if(dn==5):
        mn= 'friday'
    if(dn==6):
        mn= 'sat'
    if(dn==7):
        mn= 'sun'
    return mn

import time
for i in range(3):
    inp=int(input())
    start=time.time()
    print(printday(inp))
    print(time.time()-start)
    start=time.time()
    print(printday1(inp))
    print(time.time()-start)
