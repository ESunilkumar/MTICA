                                                                ##for all the numbers 1-100 ,use a nested
##list/dictionary comprehension to find the highest
##single digit of any of the numbers is divisibles
ans=[]
for i in range(100,111):
    temp=[]
    for j in range(1,10):
        if i%j==0:
            temp.append(j)
    ans.append([i, max(temp)])
print(ans)


asn=[]
for i in range(100,110):
    asn.append([i,max([ j for j in range(1,10)if i%j==0])])
print(asn)



lst=[]
ans=[[i,max([j for j in range(1,11)if i%j==0])] for i in range(100,110)]
print(ans)



