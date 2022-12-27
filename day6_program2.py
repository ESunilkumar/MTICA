lsteven=[]
lstodd=[]
while(True):
    inpNum=int(input("enter value(-1 to end):"))
    if inpNum==-1:
        break
    elif inpNum%2==0:
        lsteven.append(inpNum)
    elif inpNum%2==1:
        lstodd.append(inpNum)
        
print("even:",*lsteven)
print("max",max(lsteven))
print("min:",min(lsteven))
print("avg",round(sum(lsteven)/len(lsteven)),1)


print("odd:",*lstodd)
print("max",max(lstodd))
print("min:",min(lstodd))
print("avg",round(sum(lstodd)/len(lstodd)),1)


