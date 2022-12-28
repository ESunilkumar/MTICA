#remove empty strings
lst1=["sedan","suv","","","pickup",'','']

ans=[]
ans=[i for i in lst1 if i]
print(ans)
for i in lst1:
   if i:
       ans.append(i)
print(ans)
