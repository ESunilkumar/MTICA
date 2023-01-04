def sum_num(x):
    res=0
    for i in range(x+1):
        res=res+i
        yield ("i=",i,"res=",res)
    return res
z=int(input("enter value:"))
ob=sum_num(z)

for i in range(z+1):
    print(next(ob))
