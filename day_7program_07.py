lst=[10,15,20,25,30,36,45,47]

temp=[]
temp=[i+6 for i in lst]


for i in lst:
    temp.append(i+6)
print(temp)

#square of
lst1=[10,20,30,40,45,47]
test=[]
test=[i**2 for i in lst1]
print(test)


#square root
lss=[12,16,4,9,25,1,36,7,49]
two=[]
two=[round(i**0.5) for i in lss]
print(two)

lss1=[12,13,16,17,28,36,49]
tem=[]
for i in lss1:
    tem.append(round(i**0.5))

print(tem)
    

