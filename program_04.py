import math
def checkarm(num):
    n=str(num)
    total=0
    for i in n:
        total += math.pow(int(i),len(n))
    if int(n)== total:
        return 1
    else:
        return 0
num=input("enter number:")
if checkarm(num):
    print("yes")
else:
    print("no")
