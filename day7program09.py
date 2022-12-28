
dict1={"sedan":1500,"suv":2000,"pickup":2500,"minivan":1600,"van":2400,"semi":13600,"Bicycle":7,"motorcycle":110}

lst=[]
lst=[i.upper()for i in dict1 if dict1[i]<5000]
print(lst)
for i in dict1:
    if  dict1[i]<5000:
        lst.append(i.upper)
print(lst)
