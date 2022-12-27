lst=[]
while(True):
    inpNum=int(input("enter value(0 to end):"))
    if inpNum==0:
        break
    else:
        lst.append(inpNum)
lst.sort()
print("max",lst[-1])
print("min:",lst[0])
print("avg",round(sum(lst)/len(lst)),1)

