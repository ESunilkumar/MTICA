import random as r
#print(random())
#randint returns int value is a
print(r.randint(10,100))

#uniform returns float value
print(r.uniform(10,20))
      
items=[1,2,3,4]
x=r.sample(items,2)
print("x=",x)
print(x[0])
y=r.sample(items,3)
print(y)
