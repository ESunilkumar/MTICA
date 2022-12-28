import math
nums=[11,22,33,44,55]
res=[]
for i in nums:
    res.append(math.sqrt(i))
print(res)


mes=[]
mes=[math.sqrt(i) for i in nums]
print(mes)

nums=[11,22,33,44,55,2]
print(nums)
des=[]
des=list(map(math.sqrt,nums))
print(des)
